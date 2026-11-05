from wikibot import get_summary, scrape
from click.testing import CliRunner


def test_get_summary(monkeypatch):
    def fake_summary(name, sentences):
        return "Microsoft is a technology company."

    monkeypatch.setattr("wikibot.wikipedia.summary", fake_summary)

    result = get_summary("Microsoft", 1)

    assert result == "Microsoft is a technology company."


def test_scrape_cli(monkeypatch):
    """Verify that CLI arguments reach the underlying function."""

    def fake_get_summary(name, length):
        assert name == "Microsoft"
        assert length == 3
        return "Microsoft is a technology company."

    monkeypatch.setattr("wikibot.get_summary", fake_get_summary)

    runner = CliRunner()
    result = runner.invoke(scrape, ["--name", "Microsoft", "--length", "3"])

    assert result.exit_code == 0
    assert "Microsoft is a technology company." in result.output


def test_cli_help():
    """Verify that the CLI exposes help information."""

    runner = CliRunner()
    result = runner.invoke(scrape, ["--help"])

    assert result.exit_code == 0
    assert "--name" in result.output
    assert "--length" in result.output


def test_invalid_length():
    """Verify that Click rejects invalid argument types."""

    runner = CliRunner()
    result = runner.invoke(scrape, ["--name", "Microsoft", "--length", "abc"])

    assert result.exit_code != 0
    assert "Invalid value" in result.output
