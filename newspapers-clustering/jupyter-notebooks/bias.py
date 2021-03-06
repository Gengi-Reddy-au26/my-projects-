
from enum import Enum

class SimplifiedBias(Enum):
    LEFT = 0
    UNBIASED = 1
    RIGHT = 2
    
    @staticmethod
    def get_simplified_bias_for_domain(domain):
        return bias_to_simplified_bias[Bias.get_bias_for_domain(domain)]
    

class Bias(Enum):
    EXTREME_LEFT = 0
    LEFT = 1
    LEFT_CENTER = 2
    LEAST_BIASED = 3
    RIGHT_CENTER = 4
    RIGHT = 5
    EXTREME_RIGHT = 6

    @staticmethod
    def get_bias_for_domain(domain):
        return bias_by_domain[domain]

bias_to_simplified_bias = {
    Bias.EXTREME_LEFT : SimplifiedBias.LEFT,
    Bias.LEFT : SimplifiedBias.LEFT,
    Bias.LEFT_CENTER : SimplifiedBias.UNBIASED,
    Bias.LEAST_BIASED : SimplifiedBias.UNBIASED,
    Bias.RIGHT_CENTER : SimplifiedBias.UNBIASED,
    Bias.RIGHT : SimplifiedBias.RIGHT,
    Bias.EXTREME_RIGHT : SimplifiedBias.RIGHT
}

bias_by_domain = {
    'dailykos.com': Bias.EXTREME_LEFT,
    'talkingpointsmemo.com': Bias.LEFT,
    'politicususa.com': Bias.LEFT,
    'thenation.com': Bias.LEFT,
    'motherjones.com': Bias.LEFT,
    'occupydemocrats.com': Bias.EXTREME_LEFT,
    'rawstory.com': Bias.LEFT,
    'propublica.org': Bias.LEFT_CENTER,
    'thenewcivilrightsmovement.com': Bias.LEFT,
    'mediamatters.org': Bias.LEFT,
    'slate.com': Bias.LEFT,
    'thinkprogress.org': Bias.LEFT,
    'oppositionreport.com': Bias.EXTREME_LEFT,
    'democracynow.org': Bias.LEFT,
    'washingtonpost.com/blogs/plum-line': Bias.LEFT_CENTER,
    '100percentfedup.com': Bias.EXTREME_RIGHT,
    'cnn.com': Bias.LEFT_CENTER,
    'bbc.com': Bias.LEFT_CENTER,
    'bloomberg.com': Bias.LEFT_CENTER,
    'nytimes.com': Bias.LEFT_CENTER,
    'forbes.com': Bias.RIGHT_CENTER,
    'abcnews.go.com': Bias.LEFT_CENTER,
    'wsj.com': Bias.RIGHT_CENTER,
    'latimes.com': Bias.LEFT_CENTER,
    'washingtonpost.com': Bias.LEFT_CENTER,
    'nydailynews.com': Bias.LEFT_CENTER,
    'sfchronicle.com': Bias.LEFT_CENTER,
    'nypost.com': Bias.RIGHT_CENTER,
    'chicagotribune.com': Bias.LEFT_CENTER,
    'nj.com': Bias.LEFT_CENTER,
    'chicago.suntimes.com': Bias.LEFT_CENTER,
    'chron.com': Bias.LEFT_CENTER,
    'dallasnews.com': Bias.RIGHT_CENTER,
    'seattletimes.com': Bias.LEFT_CENTER,
    'azcentral.com': Bias.RIGHT_CENTER,
    'c-span.org': Bias.LEAST_BIASED,
    'economist.com': Bias.LEAST_BIASED,
    'reuters.com': Bias.LEAST_BIASED,
    'ft.com': Bias.LEAST_BIASED,
    'apnews.com': Bias.LEAST_BIASED,
    'afp.com': Bias.LEAST_BIASED,
    'usatoday.com': Bias.LEAST_BIASED,
    'townhall.com': Bias.RIGHT,
    'dailycaller.com': Bias.RIGHT,
    'breitbart.com': Bias.RIGHT,
    'dailywire.com': Bias.RIGHT,
    'conservativetribune.com': Bias.EXTREME_RIGHT,
    'thefederalistpapers.org': Bias.EXTREME_RIGHT,
    'truthfeed.com': Bias.EXTREME_RIGHT,
    'www1.cbn.com': Bias.RIGHT,
    'ijr.com': Bias.RIGHT,
    'freedomdaily.com': Bias.EXTREME_RIGHT,
    'washingtonexaminer.com': Bias.RIGHT_CENTER,
    'allenbwest.com': Bias.RIGHT,
    'theblaze.com': Bias.RIGHT,
    'louderwithcrowder.com': Bias.RIGHT,
    'mrctv.org': Bias.RIGHT,
    'rightwingnews.com': Bias.EXTREME_RIGHT,
    'westernjournalism.com': Bias.RIGHT,
    'judicialwatch.org': Bias.RIGHT,
    'thegatewaypundit.com': Bias.EXTREME_RIGHT,
    'conservative101.com': Bias.EXTREME_RIGHT,
    'bizpacreview.com': Bias.RIGHT,
    'usherald.com': Bias.EXTREME_RIGHT,
    'redstate.com': Bias.RIGHT,
    'youngcons.com': Bias.RIGHT
}
