import subprocess


def test_your_binary():
    result = subprocess.run(['./src/your_binary'], capture_output=True, text=True)
    assert result.returncode == 0  # Ensure it runs without error
