from app.prompts.hr_prompt import HR_PROMPT


def test_prompt_formats_correctly():
    prompt = HR_PROMPT.format(
        context="Test context",
        question="Test question"
    )

    assert "Test context" in prompt
    assert "Test question" in prompt