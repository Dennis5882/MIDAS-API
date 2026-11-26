"""Measure how well docs/index/chunks.jsonl answers lookup questions (BM25, no AI, no embeddings).

Questions are generated from the official articles only (seeded, so runs are comparable):
  key       "<article title> <row description>"  -> a retrieved chunk must come from that article's
            endpoint AND contain the row's Key.
  endpoint  "<article title>"                     -> a retrieved chunk must belong to that article.

BM25 is a deliberately plain baseline. A vector search should do at least as well on the same chunks;
the numbers here say whether the chunks and metadata are usable, not how good a particular RAG stack is.

  python eval_retrieval.py            # build questions if missing, score, print
  python eval_retrieval.py --rebuild  # regenerate docs/index/eval_questions.json
"""
import argparse
import collections
import json
import math
import os
import random
import re
import sys

from check_coverage import TOC_ARTICLE_ID, fetch_bodies
from om_parse import spec_rows

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
INDEX = os.path.join(ROOT, "docs", "index")
QUESTIONS = os.path.join(INDEX, "eval_questions.json")
TOKEN = re.compile(r"[A-Za-z0-9가-힣]+")


def tokens(text):
    out = []
    for word in re.findall(r"[A-Za-z0-9_\-가-힣]+", text):
        low = word.lower()
        out.append(low)
        if "_" in low or "-" in low:
            out += [p for p in re.split(r"[_\-]", low) if p]
    return out


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.tf = [collections.Counter(d) for d in docs]
        self.len = [len(d) for d in docs]
        self.avg = sum(self.len) / len(docs)
        df = collections.Counter(t for d in self.tf for t in d)
        n = len(docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        self.inv = collections.defaultdict(list)
        for i, d in enumerate(self.tf):
            for t in d:
                self.inv[t].append(i)

    def top(self, query, k=10):
        score = collections.defaultdict(float)
        for t in set(query):
            idf = self.idf.get(t)
            if not idf:
                continue
            for i in self.inv[t]:
                f = self.tf[i][t]
                score[i] += idf * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
        return sorted(score, key=score.get, reverse=True)[:k]


def build_questions(n_key=150, n_endpoint=100, seed=20261126):
    rnd = random.Random(seed)
    articles = fetch_bodies()
    key_pool, ep_pool = [], []
    for aid, art in sorted(articles.items()):
        if aid == TOC_ARTICLE_ID:
            continue
        rows = spec_rows(art.get("body"))
        if not rows:
            continue
        ep_pool.append({"article": aid, "query": art["title"]})
        for r in rows:
            desc = re.sub(r"\s+", " ", r["desc"])
            if len(r["keys"]) == 1 and len(desc) >= 15 and not desc.startswith("When"):
                key_pool.append({"article": aid, "key": r["keys"][0], "query": f"{art['title']} {desc}"})
    rnd.shuffle(key_pool)
    rnd.shuffle(ep_pool)
    return {"seed": seed, "key": key_pool[:n_key], "endpoint": ep_pool[:n_endpoint]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    if args.rebuild or not os.path.exists(QUESTIONS):
        with open(QUESTIONS, "w", encoding="utf-8", newline="\n") as f:
            json.dump(build_questions(), f, ensure_ascii=False, indent=1)
            f.write("\n")
    questions = json.load(open(QUESTIONS, encoding="utf-8"))
    chunks = [json.loads(line) for line in open(os.path.join(INDEX, "chunks.jsonl"), encoding="utf-8")]
    # the heading trail and endpoint list are part of what a retriever can match on
    docs = [tokens(c["heading"] + " " + " ".join(c["endpoints"]) + " " + c["text"]) for c in chunks]
    bm = BM25(docs)

    def run(kind, ok):
        ranks = []
        for q in questions[kind]:
            hit = bm.top(tokens(q["query"]), 10)
            rank = next((i + 1 for i, ci in enumerate(hit) if ok(chunks[ci], q)), None)
            ranks.append(rank)
        n = len(ranks)
        print(f"{kind:9s} n={n:4d}  hit@1 {sum(1 for r in ranks if r == 1) / n:6.1%}  "
              f"hit@5 {sum(1 for r in ranks if r and r <= 5) / n:6.1%}  hit@10 {sum(1 for r in ranks if r) / n:6.1%}")
        return ranks

    print(f"chunks: {len(chunks)}")
    run("endpoint", lambda c, q: q["article"] in c["articles"])
    ranks = run("key", lambda c, q: q["article"] in c["articles"] and f'"{q["key"]}"' in c["text"])
    miss = [q for q, r in zip(questions["key"], ranks) if not r]
    print("\nkey questions without a hit in the top 10 (sample):")
    for q in miss[:8]:
        print(f"  {q['article']} {q['key']:28s} {q['query'][:80]}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
