from mypy.test.data import DataDrivenTestCase, DataSuite


class PySparkCoreSuite(DataSuite):
    files = ["context.test"]
    required_out_section = True
    def run_case(self, testcase: DataDrivenTestCase) -> None:
        pass  # TODO
