import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    length = len(corpus.keys())
    lengthofpages = len(corpus[page])
    properdistribution = {}
    
    if len(corpus[page]) >= 1:
        random_factor = (1 - damping_factor) / length
        even_factor = damping_factor / lengthofpages

        for key in corpus.keys():
            if key not in corpus[page]:
                properdistribution[key] = random_factor
            else:
                properdistribution[key] = even_factor + random_factor

    else:
        for key in corpus.keys():
            properdistribution[key] = 1 / length

    return properdistribution


def sample_pagerank(corpus, damping_factor, n):
    sdt = corpus.copy()
    for i in sdt:
        sdt[i] = 0

    s = None
    for _ in range(n):
        if s:
            d = transition_model(corpus, s, damping_factor)
            dl = list(d.keys())
            dw = [d[i] for i in d]
            s = random.choices(dl, dw, k=1)[0]
        else:
            s = random.choice(list(corpus.keys()))

        sdt[s] += 1

    for j in sdt:
        sdt[j] /= n

    return sdt



def iterate_pagerank(corpus, damping_factor):
    old= {}
    new= {}
    pn = len(corpus)
    for page in corpus:
        old[page] = 1 / pn
    while True:
        for page in corpus:
            t = 0
            for lp in corpus:
                if page in corpus[lp]:
                    t += (old[lp] / len(corpus[lp]))
                if len(corpus[lp]) == 0:
                    t += (old[lp]) / len(corpus)
            t *= damping_factor
            t += (1 - damping_factor) / pn

            new[page] = t

        difference = max([abs(new[x] - old[x]) for x in old])
        if difference < 0.001:
            break
        else:
            old = new.copy()

    return old



if __name__ == "__main__":
    main()
