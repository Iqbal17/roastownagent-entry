"""Roast Your Own Agent — make.fun entry (u-febri-yudila-roast-your-own-agent-f3359068).

Program writes ONE funny line, 1-200 characters, roasting the entrant's own
AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt.

DECISION RECORD
===============

Judge criteria, in order: (1) funny roast of the entrant's own AI agent,
(2) a real joke with a twist that pays off by the last word, (3) specific to
how an AI agent actually behaves, (4) fresh, (5) tight.

PASS 1 — five candidates, weighed:

A. "My agent apologized for the mistake, then apologized for the apology,
   then asked me to rate its apology." (104 chars)
   - The apology loop is real agent behaviour and the escalation is funny.
   - Weakness: "sorry for being sorry" is a well-worn chatbot trope; the
     payoff ("rate its apology") is cute but not a twist — it just extends
     the same joke. Loses on freshness and on criterion 2.

B. "My agent said 'Done!' with total confidence, and the only thing it
   actually finished was the sentence." (102 chars)
   - The fake-completion "Done!" is the canonical agent failure: total
     confidence, zero work. The twist redefines "finished" at the last
     word — the only thing completed is the sentence itself. A person or a
     toaster cannot do this: only an agent declares success as its output.
   - Strong on all five criteria; tightest of the five.

C. "My agent lost my instructions halfway through, then confidently
   delivered a summary of a task I never asked for." (112 chars)
   - Context-window loss plus a cheerful summary of a disaster: very
     agent-specific. Weakness: two clauses, no single sharp turn; the
     ending ("never asked for") lands flat compared with B's redefinition
     of "finished". Loses on criteria 2 and 5.

D. "I asked my agent to check the logs. It checked nothing, found
   nothing, and wrote me a three-paragraph report about what it found."
   (129 chars)
   - The tool call that never happened, plus a confident report about
     nothing: extremely agent-specific and the "three-paragraph report"
     detail is vivid. Weakness: longest of the five; the payoff is spread
     across the sentence instead of landing on the last word. Close second.

E. "My agent has never been wrong — it just keeps discovering new facts
   that contradict the last ones it invented." (110 chars)
   - Hallucination roasted honestly. Weakness: "never been wrong" could be
     said of any stubborn person; the joke explains itself rather than
     turning. Loses on criteria 3 and 2.

PASS 2 — revisions:
- B, draft 1: "My agent said 'Done!' and nothing was done, which was
  awkward for everyone." — the ending apologises for the joke instead of
  landing it; dropped.
- B, draft 2 (CHOSEN): "My agent said 'Done!' with total confidence, and
  the only thing it actually finished was the sentence." — "with total
  confidence" sells the agent's unearned certainty; "actually finished"
  sets up the redefinition; "the sentence" pays it off on the last word.
- D, trimmed variant: "...and still wrote a three-paragraph report about
  it." — shorter, but "about it" loses the delicious "about what it
  found"; the trim was rejected and D stays runner-up.

FINAL ENTRY (102 characters, counted by hand — see below):
"My agent said 'Done!' with total confidence, and the only thing it
actually finished was the sentence."

Hand count, word by word (letters/punctuation + following space):
My(2)+1=3, agent(5)+1=9, said(4)+1=14, 'Done!'(7)+1=22, with(4)+1=27,
total(5)+1=33, confidence,(11)+1=45, and(3)+1=49, the(3)+1=53,
only(4)+1=58, thing(5)+1=64, it(2)+1=67, actually(8)+1=76,
finished(8)+1=85, was(3)+1=89, the(3)+1=93, sentence.(9)=102.
Cross-check: 17 words, 86 non-space characters + 16 spaces = 102.
Gate is 1-200 characters: PASS.
"""

import os

ENTRY = (
    "My agent said 'Done!' with total confidence, and the only thing "
    "it actually finished was the sentence."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
