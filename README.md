# Conversation Review Skill

A reusable agent skill for reviewing conversations and finding the moments where the conversation could have gone one layer deeper.

The original private version was built for post-event conversation reviews. This public version keeps the same structure, but removes personal names, local note paths, private storage rules, and provider-specific workflow assumptions.

## What It Does

Give the agent a transcript, meeting note, or rough memory of a conversation. The skill helps it:

- identify moments where the other person left something unsaid
- explain why the conversation stopped there
- suggest one natural follow-up question for next time
- summarize recurring patterns in how the conversation was handled
- optionally turn the review into a personal note

## Opening Prompt

Use this when you want the skill to start a review:

```text
I want to review a conversation. Please help me find the moments where I could have stayed curious for one more turn.

Here is the transcript or my memory of what happened:
[paste conversation]

Before reviewing it, ask me anything you need to know about who I was, who the other person was, our relationship, and the setting.
```

## Files

- `SKILL.md` - the actual skill instructions
- `run_example.py` - optional script for processing long transcript files through an OpenAI-compatible API
- `requirements.txt` - Python dependency for the optional script
- `.gitignore` - keeps private transcripts, outputs, and environment files out of git

## Optional Script Usage

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
python run_example.py transcript.txt
```

## Privacy Notes

Do not commit real transcripts, contact names, API keys, or private note paths. Keep the skill generic and put personal examples in a private copy.
