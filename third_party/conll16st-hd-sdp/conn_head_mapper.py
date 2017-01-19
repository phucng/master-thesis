#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConnHeadMapper(object):
    def __init__(self):
        self.mapping = ConnHeadMapper.DEFAULT_MAPPING

    def map_raw_connective(self, raw_connective):
        if raw_connective in self.mapping:
            head_connective = self.mapping[raw_connective]
        else:
            head_connective = self.mapping.get(raw_connective.lower(), raw_connective)
        # find the index of the head connectives
        raw_connective_token_list = [x for x in raw_connective.lower().split(' ') if len(x) > 0]
        head_connective_token_list = [x for x in head_connective.split(' ') if len(x) > 0]
        start_point = 0
        indices = []
        for head_connective_token in head_connective_token_list:
            for i in range(start_point, len(raw_connective_token_list)):
                token = raw_connective_token_list[i]
                if head_connective_token == token or \
                                head_connective_token == self.mapping.get(token, token):
                    indices.append(i)
                    start_point = i + 1
                    break
        assert (len(head_connective_token_list) == len(indices))
        return head_connective, indices

    DEFAULT_MAPPING = {
        "18 months after": "after",
        "25 years after": "after",
        "29 years and 11 months to the day after": "after",
        "A few hours after": "after",
        "About six months before": "before",
        "Accordingly": "accordingly",
        "Additionally": "additionally",
        "After": "after",
        "Afterward": "afterward",
        "Afterwards": "afterward",
        "Almost simultaneously": "simultaneously",
        "Also": "also",
        "Alternatively": "alternatively",
        "Although": "although",
        "And": "and",
        "As": "as",
        "As a result": "as a result",
        "As an alternative": "as an alternative",
        "As if": "as if",
        "As long as": "as long as",
        "As much as": "much as",
        "As soon as": "as soon as",
        "As well": "as well",
        "At least not when": "when",
        "At least when": "when",
        "Back when": "when",
        "Because": "because",
        "Before": "before",
        "Besides": "besides",
        "But": "but",
        "By comparison": "by comparison",
        "By contrast": "by contrast",
        "By then": "by then",
        "Consequently": "consequently",
        "Conversely": "conversely",
        "Earlier": "earlier",
        "Eight months after": "after",
        "Either or": "either or",
        "Even after": "after",
        "Even as": "as",
        "Even before": "before",
        "Even if": "if",
        "Even still": "still",
        "Even then": "then",
        "Even though": "though",
        "Even when": "when",
        "Even while": "while",
        "Ever since": "since",
        "Except": "except",
        "Finally": "finally",
        "Five minutes before": "before",
        "For": "for",
        "For example": "for example",
        "For instance": "for instance",
        "Further": "further",
        "Furthermore": "furthermore",
        "Hence": "hence",
        "However": "however",
        "IF": "if",
        "If": "if",
        "If only": "if",
        "If then": "if then",
        "In addition": "in addition",
        "In contrast": "in contrast",
        "In fact": "in fact",
        "In other words": "in other words",
        "In particular": "in particular",
        "In short": "in short",
        "In sum": "in sum",
        "In the end": "in the end",
        "In the first 25 minutes after": "after",
        "In the meantime": "meantime",
        "In the meanwhile": "meanwhile",
        "Indeed": "indeed",
        "Insofar as": "insofar as",
        "Instead": "instead",
        "Just after": "after",
        "Just because": "because",
        "Just five months after": "after",
        "Just when": "when",
        "Largely as a result": "as a result",
        "Later": "later",
        "Later on": "later",
        "Likewise": "likewise",
        "Meantime": "meantime",
        "Meanwhile": "meanwhile",
        "Months after": "after",
        "Moreover": "moreover",
        "Nearly two months after": "after",
        "Nevertheless": "nevertheless",
        "Next": "next",
        "Nonetheless": "nonetheless",
        "Nor": "nor",
        "Now that": "now that",
        "ONCE": "once",
        "On the contrary": "on the contrary",
        "On the one hand On the other hand": "on the one hand on the other hand",
        "On the other hand": "on the other hand",
        "Once": "once",
        "One day after": "after",
        "Only when": "when",
        "Or": "or",
        "Otherwise": "otherwise",
        "Overall": "overall",
        "Partly because": "because",
        "Perhaps because": "because",
        "Plus": "plus",
        "Previously": "previously",
        "Primarily because": "because",
        "Rather": "rather",
        "Regardless": "regardless",
        "Separately": "separately",
        "Shortly after": "after",
        "Shortly afterwards": "afterward",
        "Shortly before": "before",
        "Shortly thereafter": "thereafter",
        "Similarly": "similarly",
        "Simultaneously": "simultaneously",
        "Since": "since",
        "So": "so",
        "Soon after": "after",
        "Specifically": "specifically",
        "Still": "still",
        "Then": "then",
        "Thereafter": "thereafter",
        "Therefore": "therefore",
        "Though": "though",
        "Three months after": "after",
        "Thus": "thus",
        "Two weeks after": "after",
        "Ultimately": "ultimately",
        "Unless": "unless",
        "Until": "until",
        "WHEN": "when",
        "When": "when",
        "When and if": "when and if",
        "Whereas": "whereas",
        "While": "while",
        "Within minutes after": "after",
        "Yet": "yet",
        "a day after": "after",
        "a day or two before": "before",
        "a decade before": "before",
        "a few months after": "after",
        "a few weeks after": "after",
        "a full five minutes before": "before",
        "a month after": "after",
        "a week after": "after",
        "a week before": "before",
        "a year after": "after",
        "about a week after": "after",
        "about three weeks after": "after",
        "accordingly": "accordingly",
        "additionally": "additionally",
        "after": "after",
        "afterward": "afterward",
        "afterwards": "afterward",
        "almost before": "before",
        "almost immediately after": "after",
        "also": "also",
        "alternatively": "alternatively",
        "although": "although",
        "an average of six months before": "before",
        "and": "and",
        "apparently because": "because",
        "as": "as",
        "as a result": "as a result",
        "as if": "as if",
        "as long as": "as long as",
        "as much as": "much as",
        "as soon as": "as soon as",
        "as though": "as though",
        "as well": "as well",
        "at least partly because": "because",
        "at least until": "until",
        "at least when": "when",
        "because": "because",
        "before": "before",
        "before and after": "before and after",
        "besides": "besides",
        "but": "but",
        "by comparison": "by comparison",
        "by contrast": "by contrast",
        "by then": "by then",
        "consequently": "consequently",
        "earlier": "earlier",
        "either or": "either or",
        "else": "else",
        "especially after": "after",
        "especially as": "as",
        "especially because": "because",
        "especially if": "if",
        "especially since": "since",
        "especially when": "when",
        "even after": "after",
        "even as": "as",
        "even before": "before",
        "even if": "if",
        "even then": "then",
        "even though": "though",
        "even when": "when",
        "even while": "while",
        "ever since": "since",
        "except": "except",
        "except when": "when",
        "finally": "finally",
        "five years after": "after",
        "for": "for",
        "for example": "for example",
        "for instance": "for instance",
        "four days after": "after",
        "fully eight months before": "before",
        "further": "further",
        "furthermore": "furthermore",
        "hence": "hence",
        "however": "however",
        "if": "if",
        "if and when": "if and when",
        "if only": "if",
        "if then": "if then",
        "immediately after": "after",
        "in addition": "in addition",
        "in contrast": "in contrast",
        "in fact": "in fact",
        "in large part because": "because",
        "in other words": "in other words",
        "in part because": "because",
        "in particular": "in particular",
        "in the 3 1/2 years before": "before",
        "in the end": "in the end",
        "in the meantime": "meantime",
        "in turn": "in turn",
        "indeed": "indeed",
        "instead": "instead",
        "just 15 days after": "after",
        "just a day after": "after",
        "just a month after": "after",
        "just after": "after",
        "just as": "as",
        "just as soon as": "as soon as",
        "just because": "because",
        "just before": "before",
        "just days before": "before",
        "just eight days before": "before",
        "just minutes after": "after",
        "just until": "until",
        "just when": "when",
        "largely because": "because",
        "later": "later",
        "later on": "later",
        "less than a month after": "after",
        "lest": "lest",
        "likewise": "likewise",
        "long after": "after",
        "long before": "before",
        "mainly because": "because",
        "meanwhile": "meanwhile",
        "merely because": "because",
        "minutes after": "after",
        "more than a year after": "after",
        "moreover": "moreover",
        "much as": "much as",
        "nearly a year and a half after": "after",
        "neither nor": "neither nor",
        "nevertheless": "nevertheless",
        "next": "next",
        "nonetheless": "nonetheless",
        "nor": "nor",
        "not because": "because",
        "not only because": "because",
        "now that": "now that",
        "on the other hand": "on the other hand",
        "once": "once",
        "one day after": "after",
        "only after": "after",
        "only as long as": "as long as",
        "only because": "because",
        "only if": "if",
        "only three years after": "after",
        "only two weeks after": "after",
        "only until": "until",
        "only when": "when",
        "or": "or",
        "otherwise": "otherwise",
        "overall": "overall",
        "particularly after": "after",
        "particularly as": "as",
        "particularly because": "because",
        "particularly if": "if",
        "particularly since": "since",
        "particularly when": "when",
        "partly because": "because",
        "perhaps because": "because",
        "presumably because": "because",
        "previously": "previously",
        "primarily because": "because",
        "rather": "rather",
        "regardless": "regardless",
        "reportedly after": "after",
        "right after": "after",
        "separately": "separately",
        "seven years after": "after",
        "several months before": "before",
        "shortly after": "after",
        "shortly afterward": "afterward",
        "shortly before": "before",
        "shortly thereafter": "thereafter",
        "similarly": "similarly",
        "simply because": "because",
        "simultaneously": "simultaneously",
        "since": "since",
        "since before": "before",
        "six years after": "after",
        "so": "so",
        "so much as": "much as",
        "so that": "so that",
        "some time after": "after",
        "sometimes after": "after",
        "soon after": "after",
        "specifically": "specifically",
        "still": "still",
        "then": "then",
        "thereafter": "thereafter",
        "thereby": "thereby",
        "therefore": "therefore",
        "though": "though",
        "thus": "thus",
        "till": "till",
        "two days after": "after",
        "two days before": "before",
        "two months before": "before",
        "two weeks after": "after",
        "two years before": "before",
        "typically, if": "if",
        "ultimately": "ultimately",
        "unless": "unless",
        "until": "until",
        "usually when": "when",
        "when": "when",
        "whereas": "whereas",
        "while": "while",
        "within a year after": "after",
        "years after": "after",
        "years before": "before",
        "yet": "yet",
        "Days after": "after",
        "In stark contrast": "in contrast",
        "hours before": "before",
        "in the mean time": "in the mean time",
        "particularly": "particularly",
        "three years later": "later",
        "upon": "upon"
    }


if __name__ == '__main__':
    chm = ConnHeadMapper()



    raw_connective = "29 years and 11 months to the day after"
    head_connective, indices = chm.map_raw_connective(raw_connective)
    assert (head_connective == "after")
    assert (indices == [8])

    raw_connective = "Largely as a result"
    head_connective, indices = chm.map_raw_connective(raw_connective)
    assert (head_connective == "as a result")
    assert (indices == [1, 2, 3])
