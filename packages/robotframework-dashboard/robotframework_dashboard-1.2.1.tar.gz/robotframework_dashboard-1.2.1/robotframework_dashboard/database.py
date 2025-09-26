import sqlite3
from pathlib import Path
from .queries import *
from .abstractdb import AbstractDatabaseProcessor


class DatabaseProcessor(AbstractDatabaseProcessor):
    def __init__(self, database_path: Path):
        """This function should handle the connection to the database
        And if required the creation of the tables"""
        self.database_path = database_path
        # handle possible subdirectories before creating database with sqlite
        path = Path(self.database_path)
        path.parent.mkdir(exist_ok=True, parents=True)
        self.connection: sqlite3.Connection
        # create tables if required
        self.open_database()
        self._create_tables()
        self.close_database()

    def open_database(self):
        """This function should handle the setting of the connection to the database"""
        self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row

    def run_start_exists(self, run_start: str):
        run_rows = self.connection.cursor().execute(SELECT_RUN_STARTS_FROM_RUNS).fetchall()
        rows = []
        for row in run_rows:
            rows.append(self._dict_from_row(row))
        run_starts = [item['run_start'] for item in rows]
        return f'{run_start}' in run_starts

    def _create_tables(self):
        """Helper function to create the tables (they use IF NOT EXISTS to not override)"""

        def get_runs_length():
            return len(self.connection.cursor().execute(RUN_TABLE_LENGTH).fetchall())

        def get_suites_length():
            return len(self.connection.cursor().execute(SUITE_TABLE_LENGTH).fetchall())

        def get_tests_length():
            return len(self.connection.cursor().execute(TEST_TABLE_LENGTH).fetchall())

        def get_keywords_length():
            return len(
                self.connection.cursor().execute(KEYWORD_TABLE_LENGTH).fetchall()
            )

        # check to see if the tables already exist
        table_list = self.connection.cursor().execute(RUN_TABLE_EXISTS).fetchall()
        if len(table_list) > 0:
            # test: tags added in 0.4.3
            # run/suite/test/keyword: run_alias added in 0.6.0
            # run: path added in 0.8.1
            # suite/test: id was added in 0.8.4
            # run: metadata was added in 1.0.0
            run_table_length = get_runs_length()
            if run_table_length == 10:
                self.connection.cursor().execute(RUN_TABLE_UPDATE_ALIAS)
                self.connection.commit()
                run_table_length = get_runs_length()
            if run_table_length == 11:
                self.connection.cursor().execute(RUN_TABLE_UPDATE_PATH)
                self.connection.commit()
                run_table_length = get_runs_length()
            if run_table_length == 12:
                self.connection.cursor().execute(RUN_TABLE_UPDATE_METADATA)
                self.connection.commit()
                run_table_length = get_runs_length()

            suite_table_length = get_suites_length()
            if suite_table_length == 9:
                self.connection.cursor().execute(SUITE_TABLE_UPDATE_ALIAS)
                self.connection.commit()
                suite_table_length = get_suites_length()
            if suite_table_length == 10:
                self.connection.cursor().execute(SUITE_TABLE_UPDATE_ID)
                self.connection.commit()
                suite_table_length = get_suites_length()

            test_table_length = get_tests_length()
            if test_table_length == 9:
                self.connection.cursor().execute(TEST_TABLE_UPDATE_TAGS)
                self.connection.commit()
                test_table_length = get_tests_length()
            if test_table_length == 10:
                self.connection.cursor().execute(TEST_TABLE_UPDATE_ALIAS)
                self.connection.commit()
                test_table_length = get_tests_length()
            if test_table_length == 11:
                self.connection.cursor().execute(TEST_TABLE_UPDATE_ID)
                self.connection.commit()
                test_table_length = get_tests_length()

            keyword_table_length = get_keywords_length()
            if keyword_table_length == 10:
                self.connection.cursor().execute(KEYWORD_TABLE_UPDATE_ALIAS)
                self.connection.commit()
                keyword_table_length = get_keywords_length()
        else:
            self.connection.cursor().execute(CREATE_RUNS)
            self.connection.cursor().execute(CREATE_SUITES)
            self.connection.cursor().execute(CREATE_TESTS)
            self.connection.cursor().execute(CREATE_KEYWORDS)
            self.connection.commit()

    def close_database(self):
        """This function is called to close the connection to the database"""
        self.connection.close()

    def insert_output_data(
        self, output_data: dict, tags: list, run_alias: str, path: Path
    ):
        """This function inserts the data of an output file into the database"""
        try:
            self._insert_runs(output_data["runs"], tags, run_alias, path)
            self._insert_suites(output_data["suites"], run_alias)
            self._insert_tests(output_data["tests"], run_alias)
            self._insert_keywords(output_data["keywords"], run_alias)
        except Exception as error:
            print(
                f"   ERROR: something went wrong with the database: {error}"
            )

    def _insert_runs(self, runs: list, tags: list, run_alias: str, path: Path):
        """Helper function to insert the run data with the run tags"""
        full_runs = []
        for run in runs:
            *rest, last = run
            new_run = tuple(rest) + (",".join(tags), run_alias, str(path)) + (last,)
            full_runs.append(new_run)
        self.connection.executemany(INSERT_INTO_RUNS, full_runs)
        self.connection.commit()

    def _insert_suites(self, suites: list, run_alias: str):
        """Helper function to insert the suite data"""
        full_suites = []
        for suite in suites:
            suite = list(suite)
            suite.insert(9, run_alias)
            suite = tuple(suite)
            full_suites.append(suite)
        self.connection.executemany(INSERT_INTO_SUITES, full_suites)
        self.connection.commit()

    def _insert_tests(self, tests: list, run_alias: str):
        """Helper function to insert the test data"""
        full_tests = []
        for test in tests:
            test = list(test)
            test.insert(10, run_alias)
            test = tuple(test)
            full_tests.append(test)
        self.connection.executemany(INSERT_INTO_TESTS, full_tests)
        self.connection.commit()

    def _insert_keywords(self, keywords: list, run_alias: str):
        """Helper function to insert the keyword data"""
        full_keywords = []
        for keyword in keywords:
            keyword += (run_alias,)
            full_keywords.append(keyword)
        self.connection.executemany(INSERT_INTO_KEYWORDS, full_keywords)
        self.connection.commit()

    def get_data(self):
        """This function gets all the data in the database"""
        data, runs, suites, tests, keywords, aliases = {}, [], [], [], [], {}
        counter = 1
        # Get runs from run table
        run_rows = self.connection.cursor().execute(SELECT_FROM_RUNS).fetchall()
        for run_row in run_rows:
            row = self._dict_from_row(run_row)
            # exception made for versions before 0.6.0 without run_aliases
            if row["run_alias"] == None or row["run_alias"] == "":
                alias = f"Alias {counter}"
                aliases[row["run_start"]] = alias
                row["run_alias"] = alias
                counter += 1
            else:
                if row["run_alias"] in aliases.values():
                    alias = f"{row['run_alias']} {counter}"
                    aliases[row["run_start"]] = alias
                    row["run_alias"] = alias
                    counter += 1
                else:
                    aliases[row["run_start"]] = row["run_alias"]
            # exception made from versions before 0.8.1 without path
            if row["path"] == None:
                row["path"] = ""
            runs.append(row)
        data["runs"] = runs
        # Get suites from run table
        suite_rows = self.connection.cursor().execute(SELECT_FROM_SUITES).fetchall()
        for suite_row in suite_rows:
            row = self._dict_from_row(suite_row)
            row["run_alias"] = aliases[row["run_start"]]
            if row["id"] == None:
                row["id"] == ""
            suites.append(row)
        data["suites"] = suites
        # Get tests from run table
        test_rows = self.connection.cursor().execute(SELECT_FROM_TESTS).fetchall()
        for test_row in test_rows:
            row = self._dict_from_row(test_row)
            row["run_alias"] = aliases[row["run_start"]]
            if row["tags"] == None:
                row["tags"] = ""
            if row["id"] == None:
                row["id"] == ""
            tests.append(row)
        data["tests"] = tests
        # Get keywords from run table
        keyword_rows = self.connection.cursor().execute(SELECT_FROM_KEYWORDS).fetchall()
        for keyword_row in keyword_rows:
            row = self._dict_from_row(keyword_row)
            row["run_alias"] = aliases[row["run_start"]]
            keywords.append(row)
        data["keywords"] = keywords
        return data

    def _dict_from_row(self, row: sqlite3.Row):
        """Helper function create a dictionary object"""
        return dict(zip(row.keys(), row))

    def _get_runs(self):
        """Helper function to get the run data"""
        data = self.connection.cursor().execute(SELECT_RUN_DATA).fetchall()
        runs, names, aliases, tags = [], [], [], []
        for entry in data:
            entry = self._dict_from_row(entry)
            runs.append(entry["run_start"])
            names.append(entry["name"])
            aliases.append(entry["run_alias"])
            tags.append(entry["tags"])
        return runs, names, aliases, tags

    def list_runs(self):
        """This function gets all available runs and prints them to the console"""
        run_starts, run_names, run_aliases, run_tags = self._get_runs()
        for index, run_start in enumerate(run_starts):
            print(
                f"  Run {str(index).ljust(3, ' ')} | {run_start} | {run_names[index]}"
            )
        if len(run_starts) == 0:
            print(f"  WARNING: There are no runs so the dashboard will be empty!")

    def remove_runs(self, remove_runs: list):
        """This function removes all provided runs and all their corresponding data"""
        run_starts, run_names, run_aliases, run_tags = self._get_runs()
        console = ""
        for run in remove_runs:
            try:
                if "run_start=" in run:
                    run_start = run.replace("run_start=", "")
                    if not run_start in run_starts:
                        print(
                            f"  ERROR: Could not find run to remove from the database: run_start={run_start}"
                        )
                        console += f"  ERROR: Could not find run to remove from the database: run_start={run_start}\n"
                        continue
                    self._remove_run(run_start)
                    print(f"  Removed run from the database: run_start={run_start}")
                    console += (
                        f"  Removed run from the database: run_start={run_start}\n"
                    )
                elif "index=" in run:
                    runs = run.replace("index=", "").split(";")
                    indexes = []
                    for run in runs:
                        if ":" in run:
                            start, stop = run.split(":")
                            for i in range(int(start), int(stop) + 1):
                                indexes.append(i)
                        else:
                            indexes.append(int(run))
                    for index in indexes:
                        self._remove_run(run_starts[index])
                        print(
                            f"  Removed run from the database: index={index}, run_start={run_starts[index]}"
                        )
                        console += f"  Removed run from the database: index={index}, run_start={run_starts[index]}\n"
                elif "alias=" in run:
                    alias = run.replace("alias=", "")
                    self._remove_run(run_starts[run_aliases.index(alias)])
                    print(
                        f"  Removed run from the database: alias={alias}, run_start={run_starts[run_aliases.index(alias)]}"
                    )
                    console += f"  Removed run from the database: alias={alias}, run_start={run_starts[run_aliases.index(alias)]}\n"
                elif "tag=" in run:
                    tag = run.replace("tag=", "")
                    removed = 0
                    for index, run_tag in enumerate(run_tags):
                        if tag in run_tag:
                            self._remove_run(run_starts[index])
                            print(
                                f"  Removed run from the database: tag={tag}, run_start={run_starts[index]}"
                            )
                            console += f"  Removed run from the database: tag={tag}, run_start={run_starts[index]}\n"
                            removed += 1
                    if removed == 0:
                        print(
                            f"  WARNING: no runs were removed as no runs were found with tag: {tag}"
                        )
                        console += f"  WARNING: no runs were removed as no runs were found with tag: {tag}\n"
                else:
                    print(
                        f"  ERROR: incorrect usage of the remove_run feature ({run}), check out robotdashboard --help for instructions"
                    )
                    console += f"  ERROR: incorrect usage of the remove_run feature ({run}), check out robotdashboard --help for instructions\n"
            except:
                print(f"  ERROR: Could not find run to remove from the database: {run}")
                console += (
                    f"  ERROR: Could not find run to remove from the database: {run}\n"
                )
        return console

    def _remove_run(self, run_start: str):
        """Helper function to remove the data from all tables"""
        self.connection.cursor().execute(DELETE_FROM_RUNS.format(run_start=run_start))
        self.connection.cursor().execute(DELETE_FROM_SUITES.format(run_start=run_start))
        self.connection.cursor().execute(DELETE_FROM_TESTS.format(run_start=run_start))
        self.connection.cursor().execute(
            DELETE_FROM_KEYWORDS.format(run_start=run_start)
        )
        self.connection.commit()

    def update_output_path(self, log_path: str):
        """Function to update the output_path using the log path that the server has used"""
        console = ""
        log_name = log_path[11:]
        output_name = log_name.replace("log", "output").replace(".html", ".xml")
        data = self.connection.cursor().execute(SELECT_FROM_RUNS).fetchall()
        for entry in data:
            entry = self._dict_from_row(entry)
            if output_name in entry["path"] or log_name in entry["path"]:
                query = UPDATE_RUN_PATH.format(
                    path=log_path, run_start=entry["run_start"]
                )
                console = f"Executed query: {query}\n"
                self.connection.cursor().execute(query)
                self.connection.commit()
                break
        if console == "":
            console = f"ERROR: There was no output with the name {output_name} or {log_name} in any of the existing outputs in the database!\n"
        return console
