
def get_stopwords_regex(extra_stopwords=None, language='english'):
    regex_pattern = """\\b i \\b|\\b me \\b|\\b my \\b|\\b myself \\b|\\b we \\b|\\b our \\b|\\b ours \\b|\\b ourselves \\b|\\b you \\b|\\b you're \\b|\\b you've \\b|\\b you'll \\b|\\b you'd \\b|\\b your \\b|\\b yours \\b|\\b yourself \\b|\\b yourselves \\b|\\b he \\b|\\b him \\b|\\b his \\b|\\b himself \\b|\\b she \\b|\\b she's \\b|\\b her \\b|\\b hers \\b|\\b herself \\b|\\b it \\b|\\b it's \\b|\\b its \\b|\\b itself \\b|\\b they \\b|\\b them \\b|\\b their \\b|\\b theirs \\b|\\b themselves \\b|\\b what \\b|\\b which \\b|\\b who \\b|\\b whom \\b|\\b this \\b|\\b that \\b|\\b that'll \\b|\\b these \\b|\\b those \\b|\\b am \\b|\\b is \\b|\\b are \\b|\\b was \\b|\\b were \\b|\\b be \\b|\\b been \\b|\\b being \\b|\\b have \\b|\\b has \\b|\\b had \\b|\\b having \\b|\\b do \\b|\\b does \\b|\\b did \\b|\\b doing \\b|\\b a \\b|\\b an \\b|\\b the \\b|\\b and \\b|\\b but \\b|\\b if \\b|\\b or \\b|\\b because \\b|\\b as \\b|\\b until \\b|\\b while \\b|\\b of \\b|\\b at \\b|\\b by \\b|\\b for \\b|\\b with \\b|\\b about \\b|\\b against \\b|\\b between \\b|\\b into \\b|\\b through \\b|\\b during \\b|\\b before \\b|\\b after \\b|\\b above \\b|\\b below \\b|\\b to \\b|\\b from \\b|\\b up \\b|\\b down \\b|\\b in \\b|\\b out \\b|\\b on \\b|\\b off \\b|\\b over \\b|\\b under \\b|\\b again \\b|\\b further \\b|\\b then \\b|\\b once \\b|\\b here \\b|\\b there \\b|\\b when \\b|\\b where \\b|\\b why \\b|\\b how \\b|\\b all \\b|\\b any \\b|\\b both \\b|\\b each \\b|\\b few \\b|\\b more \\b|\\b most \\b|\\b other \\b|\\b some \\b|\\b such \\b|\\b no \\b|\\b nor \\b|\\b not \\b|\\b only \\b|\\b own \\b|\\b same \\b|\\b so \\b|\\b than \\b|\\b too \\b|\\b very \\b|\\b s \\b|\\b t \\b|\\b can \\b|\\b will \\b|\\b just \\b|\\b don \\b|\\b don't \\b|\\b should \\b|\\b should've \\b|\\b now \\b|\\b d \\b|\\b ll \\b|\\b m \\b|\\b o \\b|\\b re \\b|\\b ve \\b|\\b y \\b|\\b ain \\b|\\b aren \\b|\\b aren't \\b|\\b couldn \\b|\\b couldn't \\b|\\b didn \\b|\\b didn't \\b|\\b doesn \\b|\\b doesn't \\b|\\b hadn \\b|\\b hadn't \\b|\\b hasn \\b|\\b hasn't \\b|\\b haven \\b|\\b haven't \\b|\\b isn \\b|\\b isn't \\b|\\b ma \\b|\\b mightn \\b|\\b mightn't \\b|\\b mustn \\b|\\b mustn't \\b|\\b needn \\b|\\b needn't \\b|\\b shan \\b|\\b shan't \\b|\\b shouldn \\b|\\b shouldn't \\b|\\b wasn \\b|\\b wasn't \\b|\\b weren \\b|\\b weren't \\b|\\b won \\b|\\b won't \\b|\\b wouldn \\b|\\b wouldn't \\b|\\b india \\b|\\b xx \\b|\\b xxx \\b|\\b xxxx \\b|\\b xxxxx \\b|\\b xxxxx \\b|\\b a \\b|\\b b \\b|\\b c \\b|\\b d \\b|\\b e \\b|\\b f \\b|\\b g \\b|\\b h \\b|\\b i \\b|\\b j \\b|\\b k \\b|\\b l \\b|\\b m \\b|\\b n \\b|\\b o \\b|\\b p \\b|\\b q \\b|\\b r \\b|\\b s \\b|\\b t \\b|\\b u \\b|\\b v \\b|\\b w \\b|\\b x \\b|\\b y \\b|\\b z \\b|\\b A \\b|\\b B \\b|\\b C \\b|\\b D \\b|\\b E \\b|\\b F \\b|\\b G \\b|\\b H \\b|\\b I \\b|\\b J \\b|\\b K \\b|\\b L \\b|\\b M \\b|\\b N \\b|\\b O \\b|\\b P \\b|\\b Q \\b|\\b R \\b|\\b S \\b|\\b T \\b|\\b U \\b|\\b V \\b|\\b W \\b|\\b X \\b|\\b Y \\b|\\b Z \\b|\\b i\\b|\\b me\\b|\\b my\\b|\\b myself\\b|\\b we\\b|\\b our\\b|\\b ours\\b|\\b ourselves\\b|\\b you\\b|\\b you're\\b|\\b you've\\b|\\b you'll\\b|\\b you'd\\b|\\b your\\b|\\b yours\\b|\\b yourself\\b|\\b yourselves\\b|\\b he\\b|\\b him\\b|\\b his\\b|\\b himself\\b|\\b she\\b|\\b she's\\b|\\b her\\b|\\b hers\\b|\\b herself\\b|\\b it\\b|\\b it's\\b|\\b its\\b|\\b itself\\b|\\b they\\b|\\b them\\b|\\b their\\b|\\b theirs\\b|\\b themselves\\b|\\b what\\b|\\b which\\b|\\b who\\b|\\b whom\\b|\\b this\\b|\\b that\\b|\\b that'll\\b|\\b these\\b|\\b those\\b|\\b am\\b|\\b is\\b|\\b are\\b|\\b was\\b|\\b were\\b|\\b be\\b|\\b been\\b|\\b being\\b|\\b have\\b|\\b has\\b|\\b had\\b|\\b having\\b|\\b do\\b|\\b does\\b|\\b did\\b|\\b doing\\b|\\b a\\b|\\b an\\b|\\b the\\b|\\b and\\b|\\b but\\b|\\b if\\b|\\b or\\b|\\b because\\b|\\b as\\b|\\b until\\b|\\b while\\b|\\b of\\b|\\b at\\b|\\b by\\b|\\b for\\b|\\b with\\b|\\b about\\b|\\b against\\b|\\b between\\b|\\b into\\b|\\b through\\b|\\b during\\b|\\b before\\b|\\b after\\b|\\b above\\b|\\b below\\b|\\b to\\b|\\b from\\b|\\b up\\b|\\b down\\b|\\b in\\b|\\b out\\b|\\b on\\b|\\b off\\b|\\b over\\b|\\b under\\b|\\b again\\b|\\b further\\b|\\b then\\b|\\b once\\b|\\b here\\b|\\b there\\b|\\b when\\b|\\b where\\b|\\b why\\b|\\b how\\b|\\b all\\b|\\b any\\b|\\b both\\b|\\b each\\b|\\b few\\b|\\b more\\b|\\b most\\b|\\b other\\b|\\b some\\b|\\b such\\b|\\b no\\b|\\b nor\\b|\\b not\\b|\\b only\\b|\\b own\\b|\\b same\\b|\\b so\\b|\\b than\\b|\\b too\\b|\\b very\\b|\\b s\\b|\\b t\\b|\\b can\\b|\\b will\\b|\\b just\\b|\\b don\\b|\\b don't\\b|\\b should\\b|\\b should've\\b|\\b now\\b|\\b d\\b|\\b ll\\b|\\b m\\b|\\b o\\b|\\b re\\b|\\b ve\\b|\\b y\\b|\\b ain\\b|\\b aren\\b|\\b aren't\\b|\\b couldn\\b|\\b couldn't\\b|\\b didn\\b|\\b didn't\\b|\\b doesn\\b|\\b doesn't\\b|\\b hadn\\b|\\b hadn't\\b|\\b hasn\\b|\\b hasn't\\b|\\b haven\\b|\\b haven't\\b|\\b isn\\b|\\b isn't\\b|\\b ma\\b|\\b mightn\\b|\\b mightn't\\b|\\b mustn\\b|\\b mustn't\\b|\\b needn\\b|\\b needn't\\b|\\b shan\\b|\\b shan't\\b|\\b shouldn\\b|\\b shouldn't\\b|\\b wasn\\b|\\b wasn't\\b|\\b weren\\b|\\b weren't\\b|\\b won\\b|\\b won't\\b|\\b wouldn\\b|\\b wouldn't\\b|\\b india\\b|\\b xx\\b|\\b xxx\\b|\\b xxxx\\b|\\b xxxxx\\b|\\b xxxxx\\b|\\b a\\b|\\b b\\b|\\b c\\b|\\b d\\b|\\b e\\b|\\b f\\b|\\b g\\b|\\b h\\b|\\b i\\b|\\b j\\b|\\b k\\b|\\b l\\b|\\b m\\b|\\b n\\b|\\b o\\b|\\b p\\b|\\b q\\b|\\b r\\b|\\b s\\b|\\b t\\b|\\b u\\b|\\b v\\b|\\b w\\b|\\b x\\b|\\b y\\b|\\b z\\b|\\b A\\b|\\b B\\b|\\b C\\b|\\b D\\b|\\b E\\b|\\b F\\b|\\b G\\b|\\b H\\b|\\b I\\b|\\b J\\b|\\b K\\b|\\b L\\b|\\b M\\b|\\b N\\b|\\b O\\b|\\b P\\b|\\b Q\\b|\\b R\\b|\\b S\\b|\\b T\\b|\\b U\\b|\\b V\\b|\\b W\\b|\\b X\\b|\\b Y\\b|\\b Z\\b|\\bi \\b|\\bme \\b|\\bmy \\b|\\bmyself \\b|\\bwe \\b|\\bour \\b|\\bours \\b|\\bourselves \\b|\\byou \\b|\\byou're \\b|\\byou've \\b|\\byou'll \\b|\\byou'd \\b|\\byour \\b|\\byours \\b|\\byourself \\b|\\byourselves \\b|\\bhe \\b|\\bhim \\b|\\bhis \\b|\\bhimself \\b|\\bshe \\b|\\bshe's \\b|\\bher \\b|\\bhers \\b|\\bherself \\b|\\bit \\b|\\bit's \\b|\\bits \\b|\\bitself \\b|\\bthey \\b|\\bthem \\b|\\btheir \\b|\\btheirs \\b|\\bthemselves \\b|\\bwhat \\b|\\bwhich \\b|\\bwho \\b|\\bwhom \\b|\\bthis \\b|\\bthat \\b|\\bthat'll \\b|\\bthese \\b|\\bthose \\b|\\bam \\b|\\bis \\b|\\bare \\b|\\bwas \\b|\\bwere \\b|\\bbe \\b|\\bbeen \\b|\\bbeing \\b|\\bhave \\b|\\bhas \\b|\\bhad \\b|\\bhaving \\b|\\bdo \\b|\\bdoes \\b|\\bdid \\b|\\bdoing \\b|\\ba \\b|\\ban \\b|\\bthe \\b|\\band \\b|\\bbut \\b|\\bif \\b|\\bor \\b|\\bbecause \\b|\\bas \\b|\\buntil \\b|\\bwhile \\b|\\bof \\b|\\bat \\b|\\bby \\b|\\bfor \\b|\\bwith \\b|\\babout \\b|\\bagainst \\b|\\bbetween \\b|\\binto \\b|\\bthrough \\b|\\bduring \\b|\\bbefore \\b|\\bafter \\b|\\babove \\b|\\bbelow \\b|\\bto \\b|\\bfrom \\b|\\bup \\b|\\bdown \\b|\\bin \\b|\\bout \\b|\\bon \\b|\\boff \\b|\\bover \\b|\\bunder \\b|\\bagain \\b|\\bfurther \\b|\\bthen \\b|\\bonce \\b|\\bhere \\b|\\bthere \\b|\\bwhen \\b|\\bwhere \\b|\\bwhy \\b|\\bhow \\b|\\ball \\b|\\bany \\b|\\bboth \\b|\\beach \\b|\\bfew \\b|\\bmore \\b|\\bmost \\b|\\bother \\b|\\bsome \\b|\\bsuch \\b|\\bno \\b|\\bnor \\b|\\bnot \\b|\\bonly \\b|\\bown \\b|\\bsame \\b|\\bso \\b|\\bthan \\b|\\btoo \\b|\\bvery \\b|\\bs \\b|\\bt \\b|\\bcan \\b|\\bwill \\b|\\bjust \\b|\\bdon \\b|\\bdon't \\b|\\bshould \\b|\\bshould've \\b|\\bnow \\b|\\bd \\b|\\bll \\b|\\bm \\b|\\bo \\b|\\bre \\b|\\bve \\b|\\by \\b|\\bain \\b|\\baren \\b|\\baren't \\b|\\bcouldn \\b|\\bcouldn't \\b|\\bdidn \\b|\\bdidn't \\b|\\bdoesn \\b|\\bdoesn't \\b|\\bhadn \\b|\\bhadn't \\b|\\bhasn \\b|\\bhasn't \\b|\\bhaven \\b|\\bhaven't \\b|\\bisn \\b|\\bisn't \\b|\\bma \\b|\\bmightn \\b|\\bmightn't \\b|\\bmustn \\b|\\bmustn't \\b|\\bneedn \\b|\\bneedn't \\b|\\bshan \\b|\\bshan't \\b|\\bshouldn \\b|\\bshouldn't \\b|\\bwasn \\b|\\bwasn't \\b|\\bweren \\b|\\bweren't \\b|\\bwon \\b|\\bwon't \\b|\\bwouldn \\b|\\bwouldn't \\b|\\bindia \\b|\\bxx \\b|\\bxxx \\b|\\bxxxx \\b|\\bxxxxx \\b|\\bxxxxx \\b|\\ba \\b|\\bb \\b|\\bc \\b|\\bd \\b|\\be \\b|\\bf \\b|\\bg \\b|\\bh \\b|\\bi \\b|\\bj \\b|\\bk \\b|\\bl \\b|\\bm \\b|\\bn \\b|\\bo \\b|\\bp \\b|\\bq \\b|\\br \\b|\\bs \\b|\\bt \\b|\\bu \\b|\\bv \\b|\\bw \\b|\\bx \\b|\\by \\b|\\bz \\b|\\bA \\b|\\bB \\b|\\bC \\b|\\bD \\b|\\bE \\b|\\bF \\b|\\bG \\b|\\bH \\b|\\bI \\b|\\bJ \\b|\\bK \\b|\\bL \\b|\\bM \\b|\\bN \\b|\\bO \\b|\\bP \\b|\\bQ \\b|\\bR \\b|\\bS \\b|\\bT \\b|\\bU \\b|\\bV \\b|\\bW \\b|\\bX \\b|\\bY \\b|\\bZ \\b"""
    return regex_pattern
