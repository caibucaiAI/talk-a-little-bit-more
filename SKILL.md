---
name: conversation-review
description: |
  A conversation review skill for finding "we could have stayed here longer" moments.
  Use when the user shares a transcript, meeting note, voice-note transcript, or memory of a conversation
  and asks how they could have listened better, followed up more naturally, or gone deeper.
  Trigger phrases: "review this conversation", "what did I miss", "how could I have continued",
  "where did the conversation stop", "how can I talk better next time".
  Do not use for interview preparation, article writing, or therapy-like diagnosis.
---

# Conversation Review

Sometimes a conversation does not end because there is nothing left to say.
It ends because nobody knows where to go next.

This skill does one thing:
**find the moments where the conversation could have stayed alive for one more turn, and show what to do next time.**

---

## Opening Guide

When the user wants a review, start gently and concretely:

```text
Send me the transcript, notes, or your rough memory of the conversation.
I will look for the moments where something was left half-said, then give you a few natural follow-ups you could have used.

Before I review it, I may ask:
1. Which speaker is you?
2. Who was the other person?
3. What is your relationship?
4. What was the setting?
```

If the user has already provided the conversation, ask only the missing context questions.

---

## Intake Questions

Before reviewing, identify:

1. Which speaker is the user, especially when the transcript uses labels like "Speaker 1" and "Speaker 2".
2. Who the other person is: role, background, personality, current situation, or any relevant context.
3. What relationship they have: first meeting, friend, colleague, collaborator, customer, date, community member, etc.
4. Where the conversation happened: conference, meal, online call, interview, casual chat, work meeting, private message, etc.

These questions matter because relationship and setting decide what counts as curiosity, pressure, intimacy, or overstepping.

---

## Core Ideas

**Listen to understand, not to reply.**
Most people wait for their turn. A better review asks: what did the other person seem to want someone to notice?

**Silence is useful.**
A pause is not always awkward. Sometimes three seconds of space lets the other person finish the thought they almost withdrew.

**Conversations move across channels.**
People may speak in a practical channel, an emotional channel, or a social channel. Many deeper moments appear when someone says a practical thing with emotional weight behind it.

**A good follow-up is not just another question.**
It points to the specific thing the other person has not fully named yet.

---

## Review Logic

Read the whole conversation and do three things.

### 1. Find "stay here longer" moments

Look for:

**Vague words**
The other person says "fine", "pretty good", "not bad", "kind of", "a little", "it depends".
There may be a specific story underneath.

**Big abstract words**
The other person says "challenge", "turning point", "opportunity", "pressure", "clarity", "change".
Ask what concrete moment made them say that.

**Emotional shifts**
They become faster, quieter, more careful, more joking, or suddenly dismissive.
The tone changed before the topic did.

**Missing middle**
They describe A and C, but skip B.
The skipped part often carries the real decision, fear, conflict, or desire.

**Self-retraction**
They say "maybe I am overthinking", "it is probably nothing", "never mind", or "that sounds silly".
They may be pulling back a real thought.

### 2. Show how to continue

Do not give generic small-talk prompts.
Give the exact next sentence that would have fit the moment.

Use questions that sound curious, low-pressure, and grounded in what they just said.

### 3. Name the unfinished thread

From the conversation, infer what this person may still be trying to understand about themselves, their work, their relationship, or their decision.

Be careful: phrase this as a hypothesis, not a diagnosis.

---

## Output Format

Write the review as a personal note for the user. Use second person. Be direct, specific, and human.

```markdown
**[Person or Conversation Name] · [Date]**

[Brief context: who they are, how you know each other, and where this conversation happened.]

This conversation reached: [one sentence about whether it stayed surface-level, had real openings, or got close to depth without entering it.]

---

**Moments Where You Could Have Stayed Longer**

**Moment 1**

Them: [original line]
You: [what the user said next]

**What was left open**
[One or two sentences explaining what was available in that moment.]

1. **What you could have noticed**
[Concrete observation.]

2. **What you could have asked**
[One natural follow-up sentence.]

3. **Why this would have worked**
[Explain briefly.]

Repeat for Moment 2, Moment 3, etc.

---

**Recurring Pattern**

1. **[Pattern title]**
[Describe the pattern and where it appeared.]

2. **[Pattern title]**
[Describe the pattern and where it appeared.]

One thing to try next time: [one specific behavioral change.]
```

---

## Optional Save Behavior

If the user asks to save the review, save it to a location they provide.

Suggested filename:

```text
YYYYMMDD-[conversation-name]-conversation-review.md
```

Never assume a private note path. Never invent a personal archive location unless the user has already configured one.

---

## Keep This In Mind

When someone says "it was fine", they may not be closing the topic.
They may be waiting to see whether you are curious enough to ask what "fine" actually means.

