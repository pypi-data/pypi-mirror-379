import pytest
from ordeq_cli_runner import parse_args


class TestParseArgs:
    @pytest.mark.parametrize(
        ("args", "expected"),
        [
            (
                ("run", "--nodes", "domain_A:name_A"),
                {
                    "action": "run",
                    "nodes": ["domain_A:name_A"],
                    "pipeline": None,
                    "save": "all",
                    "hooks": [],
                },
            ),
            (
                ("run", "--nodes", "domain_A:name_A", "domain_B:name_B"),
                {
                    "action": "run",
                    "nodes": ["domain_A:name_A", "domain_B:name_B"],
                    "pipeline": None,
                    "save": "all",
                    "hooks": [],
                },
            ),
            (
                ("run", "--pipeline", "domain_Z:name_Z"),
                {
                    "action": "run",
                    "nodes": None,
                    "pipeline": "domain_Z:name_Z",
                    "save": "all",
                    "hooks": [],
                },
            ),
            (
                # This test case checks that the parser only parses known args.
                ("run", "--nodes", "domain_A:name_A", "--var", "bla"),
                {
                    "action": "run",
                    "nodes": ["domain_A:name_A"],
                    "pipeline": None,
                    "save": "all",
                    "hooks": [],
                },
            ),
            (
                ("run", "--pipeline", "domain_X:name_X", "--save", "sinks"),
                {
                    "action": "run",
                    "nodes": None,
                    "pipeline": "domain_X:name_X",
                    "save": "sinks",
                    "hooks": [],
                },
            ),
            (
                (
                    "run",
                    "--pipeline",
                    "domain_X:name_X",
                    "--hooks",
                    "x:Logger",
                ),
                {
                    "action": "run",
                    "nodes": None,
                    "pipeline": "domain_X:name_X",
                    "save": "all",
                    "hooks": ["x:Logger"],
                },
            ),
            (
                (
                    "run",
                    "--pipeline",
                    "domain_X:name_X",
                    "--hooks",
                    "x:Logger",
                    "y:Debugger",
                ),
                {
                    "action": "run",
                    "nodes": None,
                    "pipeline": "domain_X:name_X",
                    "save": "all",
                    "hooks": ["x:Logger", "y:Debugger"],
                },
            ),
        ],
    )
    def test_it_parses(self, args, expected):
        assert vars(parse_args(args)) == expected

    def test_nodes_and_pipeline_are_mutually_exclusive(self):
        with pytest.raises(SystemExit):
            parse_args(("--nodes", "bla", "--pipeline", "bluh"))
