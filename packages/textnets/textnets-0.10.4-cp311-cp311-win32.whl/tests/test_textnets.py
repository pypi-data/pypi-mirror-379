#!/usr/bin/env python

"""Tests for `textnets` package."""

import sqlite3

import numpy as np
import pandas as pd
from pytest import approx
from toolz import partial
from wasabi import msg

import textnets as tn

roughly = partial(approx, rel=0.1)


def dir_contains_one_file(path):
    """Check that provided directory contains one file."""
    return len(list(path.iterdir())) == 1


def test_corpus(corpus):
    """Test Corpus class using small data frame."""
    assert len(corpus.documents) == 7

    noun_phrases = corpus.noun_phrases()
    assert noun_phrases.sum().n == roughly(26)
    assert set(noun_phrases.columns) == {"term", "n", "term_weight"}

    noun_phrases_remove = corpus.noun_phrases(remove=["moon"])
    assert noun_phrases_remove.sum().n == roughly(22)
    assert set(noun_phrases_remove.columns) == {"term", "n", "term_weight"}

    noun_phrases_remove = corpus.noun_phrases(normalize=True)
    assert set(noun_phrases_remove.columns) == {"term", "n", "term_weight"}

    tokenized = corpus.tokenized()
    assert tokenized.sum().n == roughly(43)
    assert set(tokenized.columns) == {"term", "n", "term_weight"}

    nostem = corpus.tokenized(stem=False)
    assert set(nostem.columns) == {"term", "n", "term_weight"}

    nopunct = corpus.tokenized(remove_punctuation=False)
    assert set(nopunct.columns) == {"term", "n", "term_weight"}

    upper = corpus.tokenized(lower=False)
    assert set(upper.columns) == {"term", "n", "term_weight"}

    ngrams = corpus.ngrams(3)
    assert ngrams.sum().n == roughly(67)
    assert set(ngrams.columns) == {"term", "n", "term_weight"}


def test_corpus_duplicated(testdata):
    """Test Corpus class on series with duplicated labels."""
    s = pd.concat([testdata, testdata[:3], testdata[:2]])
    corpus = tn.Corpus(s)
    assert msg.counts["info"] == 1
    assert len(corpus.documents) == 7


def test_corpus_missing(testdata):
    """Test Corpus class on series with missing data."""
    s = pd.concat([testdata, pd.Series([None], index=["Missing"])])
    corpus = tn.Corpus(s)
    assert msg.counts["warn"] == 1
    assert len(corpus.documents) == 7


def test_corpus_czech():
    """Test Corpus class using Czech language documents."""
    s = pd.Series([
        "Holka modrooká nesedávej tam",
        "Holka modrooká nesedávej u potoka",
        "podemele tvoje oči",
        "vezme li tě bude škoda",
        "V potoce je hastrmánek",
        "V potoce je velká voda",
        "V potoce se voda točí",
        "zatahá tě za copánek",
    ])
    # This outputs a message about an uninstalled language model
    corpus = tn.Corpus(s, lang="cs")
    assert len(corpus.documents) == 8
    # This outputs a message about lacking a language model
    tokenized = corpus.tokenized()
    assert msg.counts["info"] == 3
    assert tokenized.sum().n > 8


def test_corpus_long():
    """Test parallelized NLP on a long series."""
    s = pd.Series(
        [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty",
        ]
        * 50
    )
    corpus = tn.Corpus(s)
    assert len(corpus.nlp) == 1000


def test_corpus_df(testdata):
    """Test creating a corpus from a data frame."""
    d = pd.DataFrame({"headlines": testdata, "meta": list("ABCDEFG")})
    c = tn.Corpus.from_df(d, doc_col="headlines")
    assert len(c.documents) == 7


def test_corpus_dict(testdata):
    """Test creating a corpus from a dictionary."""
    data = testdata.to_dict()
    c = tn.Corpus.from_dict(data)
    assert len(c.documents) == 7


def test_corpus_csv(tmp_path, testdata):
    """Test creating a corpus from a CSV file."""
    out = tmp_path / "corpus.csv"
    testdata.to_csv(out)
    c = tn.Corpus.from_csv(out)
    assert len(c.documents) == 7


def test_corpus_files(tmp_path, testdata):
    """Test creating a corpus from a collection of plain text files."""
    for fn, text in testdata.items():
        out = tmp_path / fn
        out.with_suffix(".txt").write_text(text)
    c = tn.Corpus.from_files(tmp_path.glob("*.txt"))
    assert len(c.documents) == 7


def test_corpus_sql(testdata):
    """Test creating a corpus from a SQL query."""
    with sqlite3.connect(":memory:") as conn:
        testdata.to_sql("headlines", conn)
        c = tn.Corpus.from_sql("SELECT * FROM headlines", conn)
    assert len(c.documents) == 7


def test_corpus_save_and_load(corpus, tmp_path):
    """Test roundtrip of saving and loading a corpus from file."""
    out = tmp_path / "out.corpus"
    corpus.save(out)
    loaded = tn.load_corpus(out)
    assert all(corpus.documents == loaded.documents)
    assert corpus.lang == loaded.lang


def test_corpus_sublinear_false(corpus):
    """Test corpus methods without using sublinear scaling for tf-idf."""
    noun_phrases = corpus.noun_phrases(sublinear=False)
    assert noun_phrases.sum().n == roughly(26)
    assert set(noun_phrases.columns) == {"term", "n", "term_weight"}


def test_textnet_save_and_load(corpus, tmp_path):
    """Test roundtrip of saving and loading a textnet from file."""
    out = tmp_path / "out.textnet"
    net = tn.Textnet(
        corpus.tokenized(),
        connected=True,
        doc_attrs={"test": {"New York Times": 1, "Los Angeles Times": 3}},
    )
    net.save(out)
    loaded = tn.load_textnet(out)
    assert net.nodes["id"] == loaded.nodes["id"]
    assert net.edges["weight"] == loaded.edges["weight"]
    assert net.summary == loaded.summary


def test_config_save_and_load(tmp_path):
    """Test roundtrip of saving and loading configuration parameters."""
    out = tmp_path / "out.params"
    defaults = tn.params.copy()
    tn.params.update({"lang": "cs", "autodownload": True})
    changed = tn.params.copy()
    tn.params.save(out)
    tn.params.update(defaults)
    tn.params.load(out)
    assert tn.params == changed


def test_textnet(corpus):
    """Test Textnet class using sample data."""
    noun_phrases = corpus.noun_phrases()

    n_np = tn.Textnet(noun_phrases)
    assert n_np.graph.vcount() > 0
    assert n_np.graph.ecount() > 0
    g_np_groups = n_np.project(node_type=tn.DOC)
    assert g_np_groups.vcount() > 0
    assert g_np_groups.ecount() > 0
    g_np_words = n_np.project(node_type=tn.TERM)
    assert g_np_words.vcount() > 0
    assert g_np_words.ecount() > 0


def test_textnet_matrix(corpus):
    """Test Textnet class using sample data."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases)
    g_np_groups = n_np.project(node_type=tn.DOC)
    crossprod = n_np.m @ n_np.m.T
    np.fill_diagonal(crossprod.values, 0)
    pd.testing.assert_frame_equal(
        g_np_groups.m, crossprod, check_names=False, check_exact=False
    )


def test_textnet_remove_weak_edges(corpus):
    """Test removing weak edges."""
    noun_phrases = corpus.noun_phrases()

    n_np = tn.Textnet(noun_phrases, remove_weak_edges=True)
    assert n_np.graph.ecount() > 0


def test_textnet_max_docs(corpus):
    """Test maximum document count."""
    noun_phrases = corpus.noun_phrases()

    n_np = tn.Textnet(noun_phrases, max_docs=3)
    assert n_np.graph.ecount() > 0


def test_textnet_cluster_strength(corpus):
    """Test cluster strength."""
    noun_phrases = corpus.noun_phrases()

    n_np = tn.Textnet(noun_phrases)
    assert n_np.cluster_strength.shape[0] > 0


def test_textnet_birank(corpus):
    """Test calculating bipartite centrality measures."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases)

    assert len(n_np.birank) == n_np.graph.vcount()
    assert len(n_np.cohits) == n_np.graph.vcount()
    assert len(n_np.hits) == n_np.graph.vcount()
    bgrm = tn.network.bipartite_rank(n_np, normalizer="BGRM", max_iter=200)
    assert len(bgrm) == n_np.graph.vcount()


def test_textnet_birank_connected(corpus):
    """Test BiRank in a connected graph."""
    n_np = tn.Textnet(corpus.tokenized(), min_docs=1, connected=True)

    assert len(n_np.birank) == n_np.graph.vcount()


def test_textnet_clustering(corpus):
    """Test calculating bipartite clustering coefficient."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases, connected=True)

    assert len(n_np.bipartite_cc) == n_np.graph.vcount()


def test_textnet_spanning(corpus):
    """Test calculating textual spanning measure."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases, connected=True)
    g_np_groups = n_np.project(node_type=tn.DOC)
    assert len(g_np_groups.spanning) == g_np_groups.graph.vcount()


def test_save(tmp_path, corpus):
    """Test Textnet graph saving."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases)
    out = tmp_path / "graph.graphml"
    n_np.save_graph(str(out))
    assert out.exists()
    assert out.stat().st_size > 1000
    assert dir_contains_one_file(tmp_path)


def test_plot(tmp_path, corpus):
    """Test Textnet plotting."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases)
    out = tmp_path / "plot-0.png"
    n_np.plot()
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_plot_layout(tmp_path, corpus):
    """Test Textnet plotting with bipartite layout and node labels."""
    noun_phrases = corpus.noun_phrases()
    n_np = tn.Textnet(noun_phrases)
    out = tmp_path / "plot-1.png"
    n_np.plot(bipartite_layout=True, label_nodes=True)
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_plot_projected(tmp_path, corpus):
    """Test ProjectedTextnet plotting."""
    n = tn.Textnet(corpus.tokenized())
    papers = n.project(node_type=tn.DOC)
    out = tmp_path / "plot-2.png"
    papers.plot(show_clusters=True, label_nodes=True)
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_plot_backbone(tmp_path, corpus):
    """Test ProjectedTextnet plotting with alpha cut."""
    n = tn.Textnet(corpus.tokenized())
    papers = n.project(node_type=tn.DOC)
    out = tmp_path / "plot-3.png"
    papers.plot(alpha=0.4, label_nodes=True)
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_plot_scaled(tmp_path, corpus):
    """Test ProjectedTextnet plotting with scaled nodes."""
    n = tn.Textnet(corpus.tokenized())
    papers = n.project(node_type=tn.DOC)
    out = tmp_path / "plot-4.png"
    papers.plot(scale_nodes_by="betweenness", label_nodes=True)
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_plot_filtered(tmp_path, corpus):
    """Test ProjectedTextnet plotting filtered labels."""
    n = tn.Textnet(corpus.tokenized())
    papers = n.project(node_type=tn.DOC)
    out = tmp_path / "plot-5.png"
    papers.plot(
        label_nodes=True,
        label_edges=True,
        node_label_filter=lambda v: v.degree() > 2,
        edge_label_filter=lambda e: e["weight"] > 0.1,
    )
    tn.savefig(out)
    assert out.exists()
    assert out.stat().st_size > 10_000
    assert dir_contains_one_file(tmp_path)


def test_html_repr(corpus):
    """Test HTML representations of the top-level module and core classes."""
    assert tn._repr_html_()
    assert corpus._repr_html_()
    assert tn.Textnet(corpus.tokenized())._repr_html_()
