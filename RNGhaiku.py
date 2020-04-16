import random
import tweepy
import tweepy 
from time import sleep
from datetime import date
import schedule, request

x = datetime.today()

a = date.today()
name = str(a)
full_name = name + ".txt"   
fw = open(full_name, "w")

##list time

syllabe1 = ['act', 'age', 'aid', 'aids', 'aim', 'air', 'apt', 'arch', 'arm', 'art', 'ask', 'aunt', 'back', 'bad', 'bag', 'bald', 'ball', 'ban', 'band', 'bang', 'bank', 'bar', 'bare', 'base', 'bath', 'bay', 'be', 'beach', 'beam', 'bean', 'bear', 'beat', 'bed', 'beer', 'beg', 'bell', 'belt', 'bench', 'bend', 'bet', 'bid', 'big', 'bike', 'bill', 'bind', 'bird', 'birth', 'bit', 'bite', 'black', 'blade', 'blame', 'bland', 'blank', 'bleak', 'blind', 'block', 'blond', 'blood', 'blow', 'blue', 'blunt', 'board', 'boast', 'boat', 'boil', 'bold', 'bomb', 'bond', 'bone', 'book', 'boom', 'boost', 'boot', 'born', 'boss', 'bounce', 'bound', 'bow', 'bowl', 'box', 'boy', 'brain', 'branch', 'brand', 'brash', 'brave', 'breach', 'bread', 'break', 'breast', 'breath', 'breathe', 'breed', 'brick', 'bridge', 'brief', 'bright', 'bring', 'brisk', 'broad', 'bronze', 'brown', 'brush', 'build', 'bulk', 'burn', 'burst', 'bus', 'bush', 'bust', 'buy', 'cab', 'cake', 'call', 'calm', 'camp', 'cap', 'car', 'card', 'care', 'carve', 'case', 'cash', 'cast', 'cat', 'catch', 'cause', 'cease', 'cell', 'chain', 'chair', 'chance', 'change', 'chap', 'charge', 'chart', 'chase', 'chat', 'cheap', 'check', 'cheek', 'cheer', 'cheese', 'cheque', 'chest', 'chief', 'child', 'chip', 'choice', 'choose', 'church', 'cite', 'claim', 'clash', 'class', 'clause', 'clay', 'clean', 'clear', 'clerk', 'cliff', 'climb', 'cling', 'clock', 'close', 'cloth', 'cloud', 'club', 'clue', 'clutch', 'co', 'coach', 'coal', 'coarse', 'coast', 'coat', 'code', 'coin', 'cold', 'come', 'cook', 'cool', 'cope', 'core', 'corp', 'cost', 'count', 'coup', 'course', 'court', 'cow', 'crack', 'craft', 'crap', 'crash', 'crawl', 'cream', 'creep', 'crew', 'crime', 'crisp', 'crop', 'cross', 'crowd', 'crown', 'crude', 'crush', 'cry', 'cu', 'cup', 'curl', 'curve', 'cut', 'cute', 'dad', 'daft', 'damp', 'dance', 'dank', 'dare', 'dark', 'date', 'day', 'dead', 'deaf', 'deal', 'dear', 'death', 'debt', 'deck', 'deem', 'deep', 'deft', 'depth', 'desk', 'die', 'dig', 'dim', 'dip', 'dire', 'disc', 'dish', 'disk', 'dna', 'do', 'dock', 'dog', 'door', 'dose', 'doubt', 'dour', 'down', 'drab', 'draft', 'drain', 'draw', 'dream', 'dress', 'drift', 'drink', 'drive', 'drop', 'drown', 'drug', 'drunk', 'dry', 'duck', 'duke', 'dull', 'dumb', 'dump', 'dust', 'ear', 'earl', 'earn', 'earth', 'ease', 'eat', 'edge', 'egg', 'elect', 'end', 'est', 'eye', 'face', 'fact', 'fade', 'fail', 'faint', 'fair', 'faith', 'fall', 'fan', 'far', 'farm', 'fast', 'fat', 'fate', 'fault', 'fear', 'fee', 'feed', 'feel', 'fence', 'fetch', 'field', 'fierce', 'fig', 'fight', 'file', 'fill', 'film', 'find', 'fine', 'firm', 'fish', 'fit', 'fix', 'flag', 'flame', 'flash', 'flat', 'flee', 'fleet', 'flesh', 'flight', 'fling', 'float', 'flood', 'floor', 'flow', 'fly', 'fold', 'folk', 'fond', 'food', 'fool', 'foot', 'force', 'form', 'foul', 'found', 'frail', 'frame', 'frank', 'fraud', 'free', 'freeze', 'french', 'fresh', 'friend', 'front', 'frown', 'fruit', 'fuck', 'fuel', 'full', 'fund', 'gain', 'game', 'gang', 'gap', 'gas', 'gasp', 'gate', 'gaunt', 'gay', 'gaze', 'gear', 'gene', 'get', 'ghost', 'gift', 'girl', 'give', 'glad', 'glance', 'glass', 'go', 'goal', 'god', 'gold', 'golf', 'good', 'grab', 'grade', 'grain', 'grand', 'grant', 'grasp', 'grass', 'grave', 'great', 'green', 'greet', 'grey', 'grim', 'grin', 'grip', 'gross', 'ground', 'group', 'grow', 'growth', 'guard', 'guess', 'guest', 'guide', 'guilt', 'gun', 'guy', 'hair', 'half', 'hall', 'halt', 'hand', 'hang', 'hard', 'harm', 'harsh', 'hat', 'hate', 'have', 'head', 'health', 'hear', 'heart', 'heat', 'heel', 'height', 'hell', 'help', 'hide', 'high', 'hill', 'hint', 'hip', 'hire', 'hit', 'hoarse', 'hold', 'hole', 'home', 'hope', 'horse', 'host', 'hot', 'hour', 'house', 'huge', 'hunt', 'hurt', 'ice', 'ill', 'in', 'inc', 'inch', 'inn', 'isle', 'jet', 'jew', 'job', 'join', 'joint', 'joke', 'joy', 'judge', 'juice', 'jump', 'just', 'keen', 'keep', 'key', 'kick', 'kid', 'kill', 'kind', 'king', 'kiss', 'kit', 'knee', 'knife', 'knit', 'knock', 'know', 'lack', 'lad', 'lake', 'lame', 'lamp', 'land', 'lane', 'large', 'last', 'late', 'laugh', 'launch', 'law', 'lay', 'lead', 'leaf', 'league', 'lean', 'leap', 'learn', 'lease', 'leave', 'left', 'leg', 'lend', 'length', 'let', 'lie', 'life', 'lift', 'light', 'like', 'limp', 'line', 'link', 'lip', 'list', 'live', 'load', 'loan', 'lock', 'long', 'look', 'lord', 'lose', 'loss', 'lot', 'loud', 'love', 'low', 'luck', 'lunch', 'lung', 'lush', 'm', 'mad', 'mail', 'make', 'male', 'man', 'map', 'march', 'mark', 'mass', 'match', 'mate', 'meal', 'mean', 'meat', 'meek', 'meet', 'melt', 'mere', 'merge', 'mess', 'mid', 'mild', 'mile', 'milk', 'mill', 'mind', 'mine', 'miss', 'mix', 'mode', 'moist', 'month', 'mood', 'moon', 'mount', 'mouse', 'mouth', 'move', 'mr', 'mrs', 'mud', 'mum', 'myth', 'nail', 'name', 'near', 'neat', 'neck', 'need', 'nerve', 'nest', 'net', 'new', 'nice', 'night', 'no', 'nod', 'noise', 'norm', 'nose', 'note', 'nude', 'numb', 'nurse', 'oak', 'oil', 'old', 'opt', 'owe', 'own', 'p', 'pace', 'pack', 'page', 'pain', 'paint', 'pair', 'pale', 'palm', 'park', 'part', 'pass', 'past', 'patch', 'path', 'pause', 'pay', 'peace', 'peak', 'peer', 'pen', 'pet', 'petrol', 'phase', 'phone', 'phrase', 'pick', 'piece', 'pig', 'pile', 'pin', 'pink', 'pipe', 'pit', 'pitch', 'place', 'plain', 'plan', 'plane', 'plant', 'plate', 'play', 'plead', 'please', 'plot', 'plump', 'plunge', 'point', 'pole', 'poll', 'pond', 'pool', 'poor', 'pop', 'pope', 'port', 'pose', 'posh', 'post', 'pot', 'pound', 'pour', 'praise', 'pray', 'press', 'price', 'pride', 'priest', 'prince', 'print', 'prize', 'prompt', 'proof', 'proud', 'prove', 'pub', 'pull', 'pure', 'push', 'put', 'quaint', 'queen', 'queer', 'quick', 'quote', 'race', 'raid', 'rail', 'rain', 'raise', 'range', 'rank', 'rape', 'rare', 'rat', 'rate', 'raw', 'reach', 'react', 'read', 'real', 'rear', 'red', 'ref', 'reign', 'rent', 'rest', 'rich', 'rid', 'ride', 'right', 'ring', 'rip', 'ripe', 'rise', 'risk', 'road', 'roast', 'rock', 'rod', 'role', 'roll', 'roof', 'room', 'root', 'rope', 'rose', 'rough', 'round', 'route', 'row', 'rub', 'rude', 'rule', 'run', 'rush', 'sack', 'sad', 'safe', 'sail', 'sake', 'salt', 'sand', 'sane', 'save', 'say', 'scale', 'scan', 'scant', 'scarce', 'scene', 'scheme', 'school', 'scope', 'score', 'scratch', 'scream', 'screen', 'sea', 'seal', 'search', 'seat', 'see', 'seed', 'seek', 'seem', 'seize', 'self', 'sell', 'send', 'sense', 'serve', 'set', 'sex', 'shade', 'shake', 'shame', 'shape', 'share', 'shed', 'sheep', 'sheer', 'sheet', 'shelf', 'shell', 'shift', 'shine', 'ship', 'shirt', 'shit', 'shock', 'shoe', 'shoot', 'shop', 'shore', 'short', 'shot', 'shout', 'show', 'shrewd', 'shrill', 'shrug', 'shut', 'shy', 'sick', 'side', 'sigh', 'sight', 'sign', 'silk', 'sin', 'sing', 'sink', 'sir', 'sit', 'site', 'size', 'skill', 'skin', 'skirt', 'sky', 'slack', 'slam', 'sleek', 'sleep', 'slick', 'slide', 'slight', 'slim', 'slip', 'slope', 'slow', 'small', 'smart', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'smug', 'snap', 'snide', 'snow', 'snug', 'soft', 'soil', 'sole', 'solve', 'son', 'song', 'sore', 'sort', 'soul', 'sound', 'sour', 'source', 'south', 'soy', 'space', 'spare', 'sparse', 'speak', 'speech', 'speed', 'spell', 'spend', 'sphere', 'spill', 'spin', 'split', 'spoil', 'spoilt', 'sport', 'spot', 'spread', 'spring', 'squad', 'square', 'squeeze', 'staff', 'stage', 'staid', 'stairs', 'stake', 'stale', 'stance', 'stand', 'star', 'stare', 'start', 'state', 'staunch', 'stay', 'steal', 'steam', 'steel', 'steep', 'stem', 'step', 'stick', 'stiff', 'still', 'stir', 'stock', 'stone', 'stop', 'store', 'storm', 'stout', 'straight', 'strain', 'strange', 'stream', 'street', 'strength', 'stress', 'stretch', 'strict', 'strike', 'string', 'strip', 'stroke', 'strong', 'stuff', 'style', 'suck', 'sue', 'suit', 'sum', 'sun', 'sure', 'swear', 'sweep', 'sweet', 'swift', 'swim', 'swing', 'switch', 'sword', 'tail', 'take', 'tale', 'talk', 'tall', 'tame', 'tank', 'tap', 'tape', 'task', 'taste', 'taut', 'tax', 'tea', 'teach', 'team', 'tear', 'tell', 'tempt', 'tend', 'term', 'test', 'text', 'thank', 'theft', 'theme', 'thick', 'thin', 'thing', 'think', 'thought', 'threat', 'throat', 'throw', 'thrust', 'tide', 'tie', 'tight', 'time', 'tin', 'tip', 'tone', 'tongue', 'tonne', 'tool', 'tooth', 'top', 'toss', 'touch', 'tough', 'tour', 'town', 'toy', 'trace', 'track', 'trade', 'train', 'trap', 'tray', 'treat', 'tree', 'trend', 'trick', 'trim', 'trip', 'trite', 'troop', 'truck', 'true', 'trust', 'truth', 'try', 'tube', 'tuck', 'tune', 'turn', 'twin', 'twist', 'type', 'urge', 'use', 'uv', 'vain', 'van', 'vast', 'vat', 'verse', 'view', 'vile', 'voice', 'void', 'vote', 'wage', 'wait', 'wake', 'walk', 'wall', 'wan', 'want', 'war', 'ward', 'warm', 'warmth', 'warn', 'wash', 'waste', 'watch', 'wave', 'way', 'weak', 'wear', 'week', 'weigh', 'weight', 'well', 'wet', 'wheel', 'while', 'white', 'whole', 'wide', 'wife', 'wild', 'will', 'win', 'wind', 'wine', 'wing', 'wipe', 'wire', 'wise', 'wish', 'wood', 'wool', 'word', 'work', 'world', 'worth', 'wound', 'wrap', 'write', 'wrong', 'wry', 'yard', 'year', 'yield', 'young', 'youth', 'zone', 'if', 'and', 'but', 'when', 'who', 'it', 'is', 'now', 'then', 'even', 'how', 'or', 'since', 'what', 'like', 'right', 'so', 'ahh', 'er', 'um']
syllabe2 = ['abbey', 'absence', 'absorb', 'abuse', 'accent', 'accept', 'access', 'account', 'accuse', 'achieve', 'acid', 'acquire', 'Acre', 'action', 'actor', 'acute', 'adapt', 'address', 'adjust', 'admire', 'admit', 'adopt', 'adult', 'advance', 'advice', 'advise', 'affair', 'affect', 'afford', 'agent', 'agree', 'aircraft', 'airline', 'airport', 'airy', 'alarm', 'album', 'alert', 'allege', 'allow', 'ally', 'alone', 'alter', 'amend', 'amount', 'ample', 'Angel', 'anger', 'Angle', 'angry', 'announce', 'answer', 'appeal', 'appear', 'apple', 'apply', 'appoint', 'approach', 'approve', 'arcane', 'argue', 'arise', 'Army', 'arouse', 'arrange', 'arrest', 'arrive', 'artist', 'arty', 'aspect', 'Assault', 'assert', 'assess', 'asset', 'assign', 'assist', 'assume', 'assure', 'attach', 'attack', 'attain', 'attempt', 'attend', 'attract', 'audit', 'author', 'autumn', 'avoid', 'await', 'award', 'baby', 'background', 'baggy', 'Balance', 'balmy', 'banking', 'basket', 'bastard', 'bathroom', 'battle', 'beauty', 'become', 'bedroom', 'Begin', 'behave', 'being', 'belief', 'believe', 'belong', 'Bible', 'billion', 'birthday', 'bishop', 'blanket', 'bloody', 'body', 'bonny', 'bonus', 'border', 'boring', 'borough', 'borrow', 'bossy', 'bother', 'bottle', 'bottom', 'bouncy', 'brainy', 'breakfast', 'breezy', 'Brother', 'bubbly', 'budget', 'builder', 'building', 'bulky', 'bumpy', 'burden', 'bureau', 'burly', 'bury', 'bushy', 'business', 'busy', 'butter', 'button', 'buyer', 'cable', 'campaign', 'canal', 'cancel', 'Cancer', 'canny', 'captain', 'capture', 'carbon', 'career', 'carpet', 'carriage', 'carry', 'castle', 'cater', 'ceiling', 'Centre', 'chairman', 'challenge', 'chamber', 'Champagne', 'channel', 'chapel', 'chapter', 'charter', 'cheeky', 'cheery', 'chicken', 'childhood', 'chilly', 'Christian', 'chunky', 'circle', 'circuit', 'city', 'classroom', 'classy', 'clever', 'client', 'climate', 'clinic', 'closure', 'clothing', 'cloudy', 'clumsy', 'Cm', 'coffee', 'collapse', 'colleague', 'collect', 'college', 'colonel', 'colour', 'column', 'combine', 'comfort', 'command', 'commence', 'comment', 'commit', 'compact', 'compare', 'compel', 'compete', 'compile', 'complain', 'complaint', 'complete', 'complex', 'comply', 'compose', 'compound', 'comprise', 'conceal', 'concede', 'conceive', 'concept', 'concern', 'concert', 'conclude', 'condemn', 'conduct', 'confer', 'confess', 'confine', 'confirm', 'conflict', 'conform', 'confront', 'confuse', 'Congress', 'connect', 'consent', 'consist', 'constraint', 'construct', 'consult', 'consume', 'contact', 'contain', 'content', 'contest', 'context', 'contract', 'contrast', 'control', 'convert', 'convey', 'convict', 'convince', 'copper', 'copy', 'corner', 'correct', 'corrupt', 'costly', 'cosy', 'cottage', 'cotton', 'council', 'counter', 'country', 'county', 'couple', 'cousin', 'cover', 'crafty', 'crazy', 'creamy', 'create', 'creature', 'credit', 'cricket', 'crisis', 'critic', 'cruel', 'crusty', 'crystal', 'cuddly', 'culture', 'cunning', 'cupboard', 'curly', 'curtain', 'custom', 'cycle', 'daddy', 'dainty', 'damage', 'danger', 'darkness', 'Darling', 'data', 'daughter', 'deadly', 'dealer', 'debate', 'decade', 'decide', 'declare', 'decline', 'decrease', 'defeat', 'defence', 'defend', 'define', 'degree', 'delay', 'delight', 'demand', 'deny', 'depart', 'depend', 'depict', 'deprive', 'derive', 'descend', 'describe', 'desert', 'deserve', 'design', 'desire', 'destroy', 'detail', 'detect', 'device', 'Devil', 'devise', 'devote', 'dictate', 'diet', 'differ', 'dingy', 'dinner', 'direct', 'dirty', 'discharge', 'disclose', 'discount', 'discourse', 'discreet', 'discuss', 'disease', 'dislike', 'dismiss', 'display', 'dispose', 'dispute', 'dissolve', 'distance', 'district', 'disturb', 'divert', 'divide', 'Divine', 'divorce', 'dizzy', 'Doctor', 'doctrine', 'dodgy', 'dollar', 'domain', 'doorway', 'dotty', 'double', 'Dowdy', 'downtown', 'dozen', 'dozy', 'drag', 'drama', 'draughty', 'drawing', 'dreamy', 'dreary', 'driver', 'drowsy', 'dumpy', 'dusky', 'dusty', 'duty', 'eagle', 'early', 'earthy', 'Easter', 'easy', 'Echo', 'edgy', 'edit', 'effect', 'effort', 'embark', 'embrace', 'emerge', 'Empire', 'employ', 'empty', 'enclose', 'endorse', 'enforce', 'engage', 'engine', 'English', 'enhance', 'enjoy', 'enquire', 'ensure', 'entail', 'enter', 'entrance', 'entry', 'equip', 'ERA', 'erect', 'error', 'escape', 'essay', 'essence', 'estate', 'evening', 'event', 'evolve', 'exceed', 'exchange', 'exclude', 'excuse', 'exert', 'exhaust', 'exist', 'expand', 'expect', 'expense', 'expert', 'explain', 'explode', 'exploit', 'explore', 'export', 'expose', 'express', 'extend', 'extent', 'extract', 'extreme', 'fabric', 'factor', 'failure', 'fancy', 'Farmer', 'fashion', 'Father', 'fatty', 'favour', 'feature', 'feeling', 'fellow', 'female', 'fibre', 'fiction', 'fiery', 'fighting', 'figure', 'filter', 'filthy', 'final', 'finance', 'finding', 'finger', 'finish', 'fire', 'fishing', 'fishy', 'fizzy', 'FL', 'flashy', 'fleshy', 'flimsy', 'floppy', 'flower', 'fluffy', 'fluid', 'focus', 'foggy', 'follow', 'football', 'forbid', 'forest', 'forget', 'forgive', 'format', 'fortune', 'forum', 'foundation', 'fraction', 'fragment', 'framework', 'freedom', 'friendly', 'friendship', 'frighten', 'frilly', 'frosty', 'fruity', 'fulfil', 'function', 'funding', 'funny', 'furry', 'fussy', 'future', 'fuzzy', 'garage', 'garden', 'gather', 'gaudy', 'gender', 'German', 'gesture', 'ghastly', 'ghostly', 'glassy', 'gloomy', 'glory', 'glossy', 'going', 'govern', 'grammar', 'grassy', 'greasy', 'greedy', 'grimy', 'gritty', 'grubby', 'gruesome', 'guideline', 'guilty', 'guitar', 'habit', 'hairy', 'handle', 'handsome', 'Handy', 'happen', 'happy', 'harbour', 'hardware', 'Hardy', 'hasty', 'hazy', 'heading', 'heady', 'healthy', 'hearing', 'hearty', 'Heaven', 'heavy', 'hefty', 'Hero', 'highlight', 'hilly', 'holder', 'holding', 'hollow', 'holy', 'homely', 'honest', 'honour', 'horror', 'hotel', 'household', 'housing', 'human', 'humour', 'hundred', 'hungry', 'hunting', 'hurry', 'husband', 'husky', 'icy', 'ignore', 'illness', 'image', 'impact', 'imply', 'import', 'impose', 'impress', 'improve', 'include', 'income', 'increase', 'incur', 'index', 'induce', 'infant', 'inform', 'injure', 'input', 'insect', 'insert', 'insight', 'insist', 'inspect', 'inspire', 'install', 'instance', 'instinct', 'instruct', 'insurance', 'intend', 'invent', 'invest', 'invite', 'involve', 'iron', 'island', 'issue', 'item', 'jacket', 'jolly', 'journal', 'journey', 'judgement', 'judgment', 'juicy', 'junction', 'jury', 'Justice', 'killer', 'kindly', 'kingdom', 'kitchen', 'knowledge', 'label', 'Labour', 'Lady', 'landing', 'landlord', 'landscape', 'language', 'lawyer', 'layer', 'lazy', 'leader', 'leaflet', 'leafy', 'learning', 'leather', 'lecture', 'leisure', 'lengthy', 'lesson', 'letter', 'level', 'licence', 'lifespan', 'lifetime', 'likely', 'limit', 'Lion', 'listen', 'lively', 'living', 'local', 'locate', 'lofty', 'logic', 'lonely', 'lorry', 'lousy', 'lovely', 'lover', 'lower', 'lowly', 'lucky', 'lumpy', 'machine', 'maintain', 'Maker', 'manage', 'manner', 'margin', 'market', 'marriage', 'marry', 'master', 'matter', 'mature', 'mayor', 'meaning', 'measure', 'meeting', 'mellow', 'member', 'mention', 'menu', 'merchant', 'merger', 'merit', 'merry', 'message', 'messy', 'metal', 'method', 'metre', 'middle', 'midnight', 'mighty', 'million', 'miner', 'minute', 'mirror', 'missile', 'mission', 'mistake', 'misty', 'mixture', 'mm', 'model', 'modest', 'module', 'moment', 'money', 'Moody', 'morning', 'mortgage', 'mother', 'motion', 'motive', 'motor', 'mountain', 'movement', 'movie', 'MP', 'MS', 'muddy', 'mummy', 'murder', 'murky', 'murmur', 'muscle', 'music', 'mutter', 'narrow', 'nasty', 'Nation', 'nature', 'naughty', 'Navy', 'needle', 'needy', 'neglect', 'neighbour', 'network', 'nightmare', 'noisy', 'notice', 'notion', 'novel', 'number', 'obey', 'object', 'obscure', 'observe', 'obtain', 'occur', 'ocean', 'offence', 'offer', 'office', 'oily', 'OK', 'omit', 'open', 'oppose', 'option', 'Order', 'organ', 'other', 'outcome', 'outline', 'output', 'overlook', 'owner', 'package', 'packet', 'painter', 'painting', 'palace', 'panel', 'panic', 'paper', 'parent', 'parish', 'partner', 'party', 'passage', 'Passion', 'patchy', 'patient', 'pattern', 'pavement', 'payment', 'PC', 'peasant', 'pension', 'people', 'perceive', 'percent', 'perform', 'permit', 'persist', 'person', 'persuade', 'perverse', 'petty', 'photo', 'picture', 'pilot', 'pity', 'plaintiff', 'planet', 'plastic', 'platform', 'player', 'pleasant', 'pleasure', 'pocket', 'poem', 'poet', 'police', 'polite', 'portrait', 'possess', 'power', 'practice', 'practise', 'prayer', 'precede', 'predict', 'prefer', 'premise', 'prepare', 'prescribe', 'presence', 'present', 'preserve', 'pressure', 'presume', 'pretend', 'pretty', 'prevail', 'prevent', 'prickly', 'princely', 'princess', 'printer', 'prison', 'problem', 'proceed', 'process', 'proclaim', 'produce', 'product', 'profile', 'profit', 'profound', 'program', 'programme', 'progress', 'project', 'promise', 'promote', 'pronounce', 'propose', 'prospect', 'protect', 'protest', 'provide', 'province', 'provoke', 'prudent', 'public', 'publish', 'punish', 'pupil', 'purchase', 'purple', 'purpose', 'pursue', 'quarter', 'question', 'quiet', 'rabbit', 'railway', 'rainy', 'reader', 'reading', 'ready', 'reason', 'Rebel', 'rebuild', 'recall', 'receipt', 'receive', 'reckon', 'record', 'recruit', 'reduce', 'refer', 'reflect', 'reform', 'refuse', 'regain', 'regard', 'regime', 'region', 'regret', 'reject', 'relate', 'relax', 'release', 'relief', 'relieve', 'rely', 'remain', 'remark', 'remind', 'remote', 'remove', 'render', 'renew', 'repair', 'repeat', 'replace', 'reply', 'report', 'request', 'require', 'rescue', 'research', 'reserve', 'resign', 'resist', 'resolve', 'resort', 'resource', 'respect', 'respond', 'response', 'restore', 'restrict', 'result', 'resume', 'retain', 'retire', 'return', 'reveal', 'reverse', 'review', 'revise', 'revive', 'reward', 'rhythm', 'riot', 'risky', 'rival', 'river', 'robust', 'rocky', 'rosy', 'routine', 'rubbish', 'ruddy', 'rumour', 'running', 'rusty', 'safety', 'salty', 'sample', 'sandwich', 'sandy', 'saving', 'scandal', 'scary', 'scatter', 'schedule', 'scholar', 'science', 'scruffy', 'sculpture', 'season', 'second', 'secret', 'section', 'sector', 'secure', 'select', 'seller', 'sentence', 'sequence', 'sergeant', 'servant', 'server', 'Service', 'session', 'setting', 'settle', 'severe', 'sexy', 'shabby', 'shadow', 'shady', 'shaky', 'shallow', 'shiny', 'shiver', 'shopping', 'shortage', 'shoulder', 'shower', 'sickly', 'signal', 'silence', 'silky', 'silly', 'silver', 'simple', 'sincere', 'Singer', 'Sister', 'sketchy', 'skimpy', 'skinny', 'sleazy', 'sleepy', 'slimy', 'sloppy', 'smelly', 'smoky', 'snappy', 'sneaky', 'snowy', 'soggy', 'soldier', 'sorry', 'Spanish', 'Speaker', 'spectrum', 'speedy', 'spending', 'spicy', 'spiky', 'spirit', 'spokesman', 'sponsor', 'spooky', 'sporty', 'sprightly', 'springy', 'squeaky', 'standard', 'standing', 'starry', 'stately', 'statement', 'station', 'statute', 'steady', 'stealthy', 'steely', 'sticky', 'stocky', 'stomach', 'stony', 'storage', 'stormy', 'story', 'stranger', 'strengthen', 'structure', 'struggle', 'student', 'study', 'stuffy', 'sturdy', 'subject', 'sublime', 'submit', 'substance', 'succeed', 'success', 'suffer', 'sugar', 'suggest', 'summer', 'summit', 'summon', 'sunny', 'supple', 'supply', 'support', 'suppose', 'suppress', 'surface', 'surprise', 'surround', 'survey', 'survive', 'suspect', 'suspend', 'sustain', 'swallow', 'swimming', 'symbol', 'symptom', 'system', 'table', 'tackle', 'tactic', 'talent', 'target', 'tasty', 'taxi', 'teacher', 'teaching', 'technique', 'temple', 'tenant', 'tension', 'terrace', 'testing', 'thesis', 'thinking', 'thirsty', 'thousand', 'threaten', 'ticket', 'tidy', 'tighten', 'timber', 'timing', 'tiny', 'tissue', 'title', 'toilet', 'topic', 'Tory', 'total', 'tourist', 'tower', 'trader', 'trading', 'traffic', 'trainer', 'training', 'transfer', 'transform', 'translate', 'transmit', 'transport', 'travel', 'treatment', 'treaty', 'tremble', 'trendy', 'trial', 'tricky', 'triumph', 'trouble', 'trustee', 'trusty', 'tunnel', 'tutor', 'TV', 'ugly', 'uncle', 'unfair', 'Union', 'unit', 'unite', 'UNIX', 'unkind', 'unsold', 'update', 'upset', 'urgent', 'user', 'valley', 'value', 'vanish', 'vary', 'vendor', 'venture', 'version', 'very', 'vessel', 'victim', 'Villa', 'Village', 'virtue', 'virus', 'vision', 'visit', 'volume', 'voter', 'wacky', 'wander', 'warning', 'wary', 'water', 'weaken', 'weakness', 'wealthy', 'weapon', 'weary', 'weather', 'wedding', 'weedy', 'weekend', 'weighty', 'welcome', 'welfare', 'whisky', 'whisper', 'widen', 'widow', 'window', 'windy', 'winner', 'winter', 'withdraw', 'witness', 'witty', 'woman', 'wonder', 'woolly', 'worker', 'working', 'workshop', 'worldly', 'worry', 'worthy', 'writer', 'writing', 'yellow', 'youngst']
syllabe3 = ['abandon', 'abolish', 'absolute', 'acceptance', 'accident', 'accountant', 'achievement', 'acknowledge', 'activate', 'addition', 'adjustment', 'admission', 'advantage', 'adventure', 'advertise', 'adviser', 'advocate', 'afternoon', 'agency', 'agenda', 'agreement', 'alcohol', 'alliance', 'allocate', 'allowance', 'ambition', 'ambulance', 'amendment', 'analyse', 'analyst', 'animal', 'announcement', 'apartment', 'appearance', 'appendix', 'applicant', 'appointment', 'approval', 'archbishop', 'architect', 'area', 'argument', 'arrangement', 'arrival', 'article', 'assemble', 'assembly', 'assessment', 'assignment', 'assistance', 'assistant', 'assumption', 'assurance', 'atmosphere', 'attendance', 'attention', 'attitude', 'attraction', 'attribute', 'audience', 'auditor', 'avenue', 'average', 'awareness', 'barrier', 'battery', 'beginning', 'behaviour', 'benefit', 'boundary', 'businessman', 'cabinet', 'calculate', 'camera', 'candidate', 'capital', 'carrier', 'casual', 'catalogue', 'cathedral', 'celebrate', 'century', 'champion', 'chancellor', 'character', 'charity', 'chemical', 'chocolate', 'cigarette', 'cinema', 'circulate', 'circumstance', 'citizen', 'clarify', 'classify', 'coincide', 'collection', 'collector', 'colony', 'commander', 'commission', 'commitment', 'committee', 'commonwealth', 'companion', 'company', 'compensate', 'completion', 'component', 'compromise', 'computer', 'concentrate', 'conception', 'concession', 'conclusion', 'condition', 'conference', 'confidence', 'confusion', 'connection', 'consciousness', 'consequence', 'consider', 'constable', 'constitute', 'construction', 'consultant', 'consumer', 'consumption', 'contemplate', 'continent', 'continue', 'contribute', 'convention', 'conversion', 'conviction', 'correspond', 'corridor', 'councillor', 'counterpart', 'coverage', 'creation', 'creditor', 'criticise', 'criticism', 'criticize', 'curious', 'currency', 'customer', 'database', 'decision', 'decorate', 'dedicate', 'defendant', 'defender', 'deficit', 'delegate', 'deliver', 'democrat', 'demonstrate', 'density', 'department', 'departure', 'deposit', 'depression', 'deputy', 'description', 'designer', 'destruction', 'detective', 'determine', 'develop', 'diagram', 'dialogue', 'diamond', 'diary', 'difference', 'dimension', 'diminish', 'direction', 'directive', 'director', 'disagree', 'disappear', 'disaster', 'discipline', 'discover', 'discretion', 'discussion', 'dismissal', 'disorder', 'disposal', 'distinction', 'distinguish', 'distribute', 'dividend', 'division', 'document', 'dominate', 'duration', 'edition', 'editor', 'educate', 'election', 'element', 'embody', 'emission', 'emotion', 'emperor', 'emphasise', 'emphasize', 'employee', 'employer', 'employment', 'enable', 'encounter', 'encourage', 'enemy', 'energy', 'engagement', 'engineer', 'enquiry', 'enterprise', 'entertain', 'entitle', 'entity', 'envelope', 'envisage', 'episode', 'equation', 'equipment', 'equity', 'establish', 'estimate', 'evidence', 'examine', 'example', 'exception', 'excitement', 'exclusion', 'execute', 'exercise', 'exhibit', 'existence', 'expansion', 'expertise', 'explosion', 'exposure', 'expression', 'extension', 'factory', 'family', 'fantasy', 'favourite', 'festival', 'formation', 'formula', 'formulate', 'frequency', 'funeral', 'furniture', 'gallery', 'general', 'generate', 'gentleman', 'government', 'governor', 'graduate', 'guarantee', 'guardian', 'heritage', 'hesitate', 'history', 'holiday', 'horizon', 'hospital', 'idea', 'illustrate', 'imagine', 'implement', 'importance', 'impression', 'improvement', 'incentive', 'incidence', 'incident', 'indicate', 'industry', 'infection', 'inflation', 'influence', 'inherit', 'inhibit', 'injury', 'inquiry', 'inspection', 'inspector', 'institute', 'instruction', 'instrument', 'integrate', 'intention', 'interest', 'interface', 'interfere', 'interpret', 'interrupt', 'interval', 'intervene', 'interview', 'introduce', 'invasion', 'investment', 'investor', 'involvement', 'isolate', 'journalist', 'justify', 'leadership', 'liberty', 'library', 'location', 'loyalty', 'magazine', 'magistrate', 'management', 'manager', 'marketing', 'measurement', 'mechanism', 'medicine', 'medium', 'membership', 'memory', 'mineral', 'minimum', 'minister', 'ministry', 'modify', 'molecule', 'monitor', 'motivate', 'multiply', 'museum', 'musician', 'mystery', 'negligent', 'newspaper', 'nursery', 'objection', 'objective', 'observer', 'occasion', 'occupy', 'offender', 'officer', 'official', 'opening', 'opera', 'operate', 'opinion', 'opponent', 'organise', 'organism', 'organize', 'origin', 'overcome', 'overnight', 'ownership', 'oxygen', 'paragraph', 'parliament', 'particle', 'partnership', 'passenger', 'penalty', 'penetrate', 'pensioner', 'percentage', 'perception', 'performance', 'period', 'permission', 'personnel', 'perspective', 'photograph', 'piano', 'poetry', 'policeman', 'policy', 'pollution', 'portfolio', 'position', 'possession', 'potato', 'potential', 'preference', 'pregnancy', 'premium', 'president', 'principle', 'prisoner', 'privilege', 'procedure', 'proceeding', 'processor', 'producer', 'production', 'profession', 'professor', 'promotion', 'property', 'proportion', 'proposal', 'protection', 'protein', 'provision', 'publisher', 'punishment', 'purchaser', 'qualify', 'quality', 'quantity', 'radio', 'ratio', 'reaction', 'realise', 'realize', 'reassure', 'receiver', 'reception', 'recession', 'recipe', 'recognise', 'recognize', 'recommend', 'recording', 'recover', 'reduction', 'reference', 'reflection', 'refugee', 'refusal', 'register', 'regulate', 'reinforce', 'relation', 'relative', 'religion', 'remedy', 'remember', 'removal', 'replacement', 'reporter', 'represent', 'reproduce', 'republic', 'requirement', 'researcher', 'resemble', 'residence', 'resident', 'resistance', 'restaurant', 'restriction', 'retirement', 'revenue', 'salary', 'satellite', 'satisfy', 'scientist', 'selection', 'seminar', 'sensation', 'separate', 'settlement', 'shadowy', 'shareholder', 'situate', 'solution', 'specialist', 'specify', 'specimen', 'stimulate', 'stimulus', 'strategy', 'studio', 'subsidy', 'substitute', 'succession', 'successor', 'suggestion', 'suicide', 'summary', 'supervise', 'supplement', 'supplier', 'supporter', 'surgery', 'survival', 'suspicion', 'sympathy', 'taxation', 'teenager', 'telephone', 'tendency', 'theatre', 'theory', 'therapy', 'tournament', 'tradition', 'tragedy', 'transaction', 'transition', 'traveller', 'treasury', 'tribunal', 'turnover', 'uncanny', 'undergo', 'underline', 'undermine', 'understand', 'undertake', 'ungainly', 'unhappy', 'uniform', 'united', 'unity', 'universe', 'unlikely', 'unlucky', 'unpleasant', 'unruly', 'untidy', 'vehicle', 'victory', 'video', 'violence', 'visitor', 'volunteer', 'withdrawal']
syllabe4 = ['ability', 'accommodate', 'accompany', 'accumulate', 'accuracy', 'acquisition', 'activity', 'administer', 'advertisement', 'agriculture', 'allegation', 'allocation', 'alternative', 'american', 'analysis', 'anticipate', 'anxiety', 'application', 'appreciate', 'architecture', 'associate', 'authority', 'autonomy', 'calculation', 'capacity', 'capitalism', 'casualty', 'category', 'celebration', 'ceremony', 'certificate', 'championship', 'characterise', 'characterize', 'coalition', 'combination', 'commissioner', 'communicate', 'community', 'comparison', 'compensation', 'competition', 'competitor', 'complexity', 'composition', 'concentration', 'conservation', 'conservative', 'constituent', 'constitution', 'consultation', 'contribution', 'controversy', 'conversation', 'corporation', 'correlation', 'correspondent', 'criterion', 'curriculum', 'declaration', 'definition', 'delegation', 'delivery', 'democracy', 'demonstration', 'developer', 'development', 'diagnosis', 'dictionary', 'difficulty', 'directory', 'disadvantage', 'disappointment', 'discovery', 'distribution', 'economy', 'education', 'efficiency', 'eliminate', 'emergency', 'engineering', 'entertainment', 'enthusiasm', 'environment', 'equivalent', 'establishment', 'evaluate', 'evolution', 'execution', 'executive', 'exhibition', 'expectation', 'expenditure', 'experience', 'experiment', 'explanation', 'facilitate', 'facility', 'federation', 'generation', 'hierarchy', 'historian', 'hypothesis', 'identify', 'identity', 'illustration', 'implication', 'incorporate', 'indication', 'indicator', 'information', 'ingredient', 'initiate', 'innovation', 'installation',
'institution', 'integration', 'intelligence', 'interaction', 'interior', 'intervention', 'introduction', 'investigate', 'invitation', 'isolation', 'jurisdiction', 'legislation', 'liberation', 'limitation', 'literature', 'machinery', 'majority', 'manipulate', 'manufacture', 'material', 'minority', 'monopoly', 'mortality', 'motivation', 'necessity', 'negotiate', 'obligation', 'observation', 'occupation', 'operation', 'operator', 'opposition', 'originate', 'participant', 'participate', 'phenomenon', 'philosophy', 'politician', 'polytechnic', 'population', 'practitioner', 'preparation', 'presentation', 'priority', 'professional', 'proposition', 'prosecution', 'psychology', 'publication', 'radiation', 'reality', 'recognition', 'recovery', 'redundancy', 'registration', 'regulation', 'relationship', 'reputation', 'resignation', 'resolution', 'restoration', 'revolution', 'satisfaction', 'secretary', 'security', 'separation', 'significance', 'situation', 'society', 'solicitor', 'speculation', 'stability', 'technology', 'television', 'temperature', 'territory', 'transformation', 'uncertainty', 'understanding', 'variable', 'variation', 'variety', 'vegetable']
syllabe5 = ['alliteration', 'California', 'unidentified', 'abomination', 'discrimination', 'personality', 'photosynthesis', 'Pennsylvania', 'exacerbation', 'syllabication', 'Constantinople', 'marijuana', 'abominable', 'anniversary', 'commensalism', 'imagination', 'serendipity', 'university', 'electricity', 'organization', 'everybody', 'curiosity', 'Louisiana', 'intimidating', 'abolitionist', 'multiplication', 'appreciation', 'Apocalypse', 'procrastination', 'communication', 'annunciation', 'excoriation', 'diabolical', 'appreciated', 'illuminati', 'invigilator', 'individual', 'mummification', 'deforestation', 'elementary', 'acceleration', 'appropriation', 'trigonometry', 'globalization', 'colonoscopy', 'communicator', 'extraordinary', 'beautician', 'generosity', 'civilization', 'abracadabra', 'velociraptor', 'californium', 'conjunctivitis', 'evaporation', 'cytoskeleton', 'representative', 'hippopotamus', 'exasperation', 'factorisation', 'equanimity', 'insignificant', 'felicitation', 'abbreviation', 'characteristics', 'acetylcholine', 'administrator', 'quadrilateral', 'colonization', 'infatuation', 'apothecary', 'representation', 'ingredients', 'depreciation', 'disambiguation', 'refrigerator', 'chemosynthesis', 'antihistamine', 'pulchritudinous', 'imaginary', 'gentrification', 'congratulations', 'patriotism', 'determination', 'Animalia', 'defenestration', 'evaluation', 'association', 'undeniable', 'pontification', 'collaboration', 'evacuation', 'cafeteria', 'hospitality', 'exhilarating', 'afforestation', 'administration', 'interpretation', 'unconditional', 'radioactive', 'awesomeness', 'elimination', 'Philadelphia', 'orientation', 'pericarditis', 'paleontologist', 'confederation', 'ratiocination', 'anticipated', 'thermochemistry', 'circulatory', 'schizophrenia', 'alliterative', 'globalisation', 'cytokinesis', 'mathematician', 'americium', 'inequality', 'respiratory', 'laboratory', 'polynomial', 'vocabulary', 'intolerable', 'factorization', 'Balenciaga', 'International', 'accommodating', 'anthropomorphize', 'echolocation', 'opportunity', 'encouragement', 'beautifully', 'plagiarism', 'hypothalamus', 'uncomparable', 'supercilious', 'colonisation', 'agribusiness', 'scarification', 'intellectual', 'kleptomania', 'absentmindedness', 'supernatural', 'methamphetamine', 'understandable', 'finalisation', 'reforestation', 'hypothermia', 'vegetarian', 'interdependence', 'humiliation', 'excruciating', 'consanguinity', 'degeneration', 'antioxidant', 'ameliorate', 'regimentation', 'inspirational', 'recrimination', 'reliableness', 'sociology', 'Mediterranean', 'asphyxiation', 'abbreviated', 'unprepossessing', 'idealisation', 'annihilation', 'multiprogramming', 'irreplaceable', 'unattainable', 'paramecium', 'cosmetologist', 'equilibrium', 'gadolinium', 'unacceptable', 'specialization', 'necrophilia', 'accommodation', 'electrolysis', 'animosity', 'archaeology', 'adulteration', 'paraphilia', 'sectionalism', 'possibilities', 'classification', 'ramification', 'consumerism', 'cardiology', 'accreditation', 'aerodynamics', 'Sagittarius', 'telekinesis', 'Thessalonica', 'absenteeism', 'stoichiometry', 'lithification', 'alliterating', 'politician', 'equivocating', 'equivocation', 'ratification', 'monophobia', 'parallelogram', 'teleprocessing', 'bureaucracy', 'ankylosaurus', 'pandemonium', 'acrimonious', 'precipitation', 'auditorium', 'infidelity', 'rejuvenation', 'unrelatable', 'astronomical', 'foreseeable', 'amortization', 'extenuating', 'disoriented', 'immunization', 'accelerator', 'intoxication', 'accidentally', 'neutralization', 'pediatrician', 'resilient', 'transubstantiation', 'misunderstanding', 'praseodymium', 'Aboriginal', 'prognostication', 'authoritative', 'confederacy', 'amelioration', 'ecotourism', 'biochemistry', 'impecunious', 'equilateral', 'adjudication', 'ridiculousness', 'acrocyanosis', 'biological', 'irresponsible', 'hereditary', 'telecommuting']
syllabe6 = ['saponification', 'abiogenesis', 'capitalization', 'biodiversity', 'trichomoniasis', 'responsibility', 'personification', 'prestidigitation', 'voluminosity', 'plasmodesmata', 'desertification', 'extraterrestrial', 'capitalisation', 'Abecedarian', 'Mesopotamia', 'accountability', 'electrifying', 'imperialism', 'veterinarian', 'indefatigable', 'alphabetisation', 'collectivization', 'bioterrorism', 'dimethyltryptamine', 'encyclopedia', 'identification', 'revolutionary', 'Acanthisittidae', 'characterization', 'benzodiazepine', 'sphygmomanometer', 'generalization', 'beneficiary', 'biotechnology', 'amniocentesis', 'antidiabetic', 'enthusiastically', 'antepenultimate', 'acclimatization', 'archaebacteria', 'hydroelectricity', 'humanitarian', 'abdominoplasty', 'autobiography', 'identifiable', 'rationalisation', 'Australopithecus', 'characteristically', 'initialisation', 'adaptability', 'bioluminescence', 'atherosclerosis', 'apprehensiveness', 'anaplasmosis', 'syllabification', 'abecedarius', 'idiosyncrasy', 'invisibility', 'cardiovascular', 'parthenogenesis', 'alienation', 'beautification', 'acceptability', 'involuntarily', 'bacteriology', 'tintinnabulation', 'acanthocytosis', 'acclimatisation', 'acetaminophen', 'dependability', 'hyperglycemia', 'discombobulated', 'counterrevolution', 'biodegradable', 'accelerometer', 'Americanism', 'responsibilities', 'megalomania', 'behaviorism', 'labialization', 'rehabilitation', 'familiarity', 'abecedarium', 'australopithecine', 'reconciliation',
'acetonemia', 'nationalisation', 'integumentary', 'insubordination', 'actinomycosis', 'gastroenterologist', 'dermatosclerosis', 'divisibility', 'maladministration', 'Adiantaceae', 'excommunication', 'academicism', 'reliability', 'idiosyncratic', 'applicability', 'ameliorated', 'accompanying', 'extemporaneous', 'misrepresentation', 'hypokalemia', 'medicamentation', 'confidentiality', 'specificality', 'internalization', 'polymerization', 'nanotechnology', 'paraphernalia', 'artificiality', 'beautifying', 'antemeridian', 'anathematizing', 'misappreciation', 'anticoagulation', 'naturalization', 'animalisation', 'disorientation',
'misadministration', 'alienator', 'memorabilia', 'diverticulitis', 'chemiluminescence', 'colonialism', 'congeniality', 'rationalization', 'mycobacterium', 'Radiolaria', 'acquisitiveness', 'nationalization', 'eventuality', 'homogenization', 'admissibility', 'bioremediation', 'hyponatremia', 'agrarianism', 'characterisation', 'polymerisation', 'commercialization', 'toxoplasmosis', 'irreconcilable', 'anticholinergic', 'environmentalist', 'dehumanization', 'vulnerability',
'ammonification', 'fundamentalism', 'prenotification', 'familiarizing', 'liberalization', 'deniability', 'depolarization', 'transcendentalism', 'Indianapolis', 'detoxification', 'superannuated', 'abortifacient', 'anthropocentrism', 'hypercalcemia', 'cinematography', 'microbiology', 'naturalisation', 'experimentation', 'autointoxication', 'Agaricaceae', 'purificatory', 'actualization', 'episiotomy', 'electrification', 'bioengineering', 'availability', 'irrationality', 'infinitesimal', 'appropriateness', 'alphabetization', 'overcompensation', 'administratively', 'identifying', 'cholecystectomy', 'individuating', 'abominableness', 'antibacterial', 'aktiengesellschaft', 'originality', 'accommodatingly', 'approximatively', 'onomatopoetic', 'cholelithiasis', 'macaronicism', 'epididymitis', 'marginalization', 'archaeological']
syllabe7 = ['abdominocentesis', 'onomatopoeia', 'abdominovesical', 'interdisciplinary', 'industrialization', 'hyperlipidemia', 'Americanization', 'anesthesiologist', 'collaborativeness', 'maneuverability', 'industrialisation', 'undemonstrativeness', 'decriminalization', 'individuality', 'denationalization', 'Armadillidiidae', 'anesthesiology', 'buckminsterfullerene', 'telecommunication', 'anathematization', 'Caesalpinioideae', 'demasculinization', 'miniaturization', 'unilateralism', 'compartmentalization', 'antinomianism', 'electrophotometer', 'oversimplification', 'abalienation', 'academicianship', 'associationism', 'Americanisation', 'Aquifoliaceae', 'familiarization', 'triskaidekaphobia', 'anthropocentricity', 'abominability', 'emotionalization', 'inaccessibility', 'familiarisation', 'corynebacterium', 'adventuresomeness', 'intellectuality', 'neurofibromatosis', 'compartmentalisation', 'imponderability', 'conventionalization', 'anathematisation', 'antiquarianism', 'materialisation', 'misidentification', 'environmentalism', 'inalienable', 'remilitarization', 'individualizing', 'conceptualization',
'phantasmagoria', 'multiculturalism', 'automysophobia', 'autoplagiarism', 'memorialization', 'materialization', 'glomerulonephritis', 'Hymenophyllaceae', 'demythologisation', 'Acnidosporidia', 'hypoproteinemia', 'imperfectability', 'Mastigomycotina', 'appendicularia', 'neocolonialism', 'impracticability', 'impecuniosity', 'Phalacrocoracidae', 'unindustrialized', 'Basidiomycota', 'Actinidiaceae', 'conceptualisation', 'Ancylostomatidae', 'arteriosclerosis', 'septuagenarian', 'depersonalization', 'particularisation', 'uncharacteristically', 'Liliuokalani', 'depersonalisation', 'antiredeposition', 'undiscriminatingness', 'foreseeability', 'pachycephalosaurus', 'heterogeneousness', 'denationalisation', 'Anacardiaceae', 'imperfectibility', 'epidemiology', 'angiotelectasia', 'unidentifiable', 'miniaturisation', 'electromagnetism', 'unfamiliarity', 'discriminativeness', 'irresponsibility', 'demineralisation', 'encephalomyelitis', 'manoeuvrability', 'electrocardiograph', 'demineralization', 'intercommunication', 'adenocarcinoma', 'libertarianism', 'neurobiological', 'anticholinesterase', 'adenohypophysis', 'agranulocytosis', 'unalterability', 'laryngopharyngitis', 'unsubstantialization', 'chemicoluminescence', 'particularization', 'interaffiliated', 'decriminalisation', 'individualism', 'Marginocephalia', 'batrachomyomachia', 'overenthusiastic', 'trichotillomania', 'Alstroemeriaceae', 'Cercidiphyllaceae', 'counterproductiveness', 'onomatopoetically', 'Machiavellianism', 'unexperiencedness', 'irreducibility', 'Alismataceae', 'aboriginality', 'phantasmagorical', 'sentimentalization', 'incalculability', 'ultracentrifugation', 'Amaryllidaceae', 'asclepiadaceous', 'cephalohematoma', 'colloquialism', 'Rastafarianism', 'spiritualisation', 'semiautomatic', 'electroencephalograph', 'imaginativeness', 'Caprifoliaceae', 'indefinability', 'demilitarization', 'desynonymization', 'crystalloluminescence', 'intelligibility', 'authoritativeness', 'immaterialism', 'unalienable', 'Albigensianism', 'indestructibility', 'ariboflavinosis', 'memorialisation', 'unmanageability', 'photodisintegration', 'appreciativeness', 'coccidiomycosis', 'argumentativeness', 'overambitiousness', 'cytomegalovirus', 'thrombocytopenia', 'indefatigableness', 'chemicobiology', 'hypervitaminosis', 'aristocraticalness', 'Chenopodiaceae', 'choriomeningitis', 'Acanthopterygii', 'Presbyterianism', 'Avicenniaceae', 'autobiographical', 'underevaluation', 'Cilioflagellata', 'anisometropia', 'Tricholomataceae', 'disagreeability', 'psychogalvanometer', 'unintoxicatedness', 'unserviceability', 'Convallariaceae', 'irreproachability', 'basidiomycetous', 'radioactivity', 'comprehensibility', 'overpatriotism', 'hydrochlorothiazide', 'hemoglobinemia']

list_of_lists1 = [syllabe1, syllabe2, syllabe3, syllabe4, syllabe5]

list_of_lists2 = [syllabe1, syllabe2, syllabe3, syllabe4, syllabe5, syllabe6, syllabe7]

haikulineone = ""
haikulinetwo = ""
haikulinethree = ""

def line1():
    global haikulineone
    haiku1 = []
    line_syllable = 0
    if line_syllable == 0:
        #while line syllable = 0: - not so elegant and would mean a LOT of lines
        word_choice = random.choice(list_of_lists1[0:4])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        elif word_choice == syllabe5:
            line_syllable +=5        
        word_select = random.choice(word_choice)
        haiku1.append(word_select)
    if line_syllable == 1:
        word_choice = random.choice(list_of_lists1[0:3])
        if word_choice in haiku1:
            haiku1.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku1.append(word_select)
    if line_syllable == 2:
        word_choice = random.choice(list_of_lists1[0:2])
        if word_choice in haiku1:
            haiku1.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku1.append(word_select)
    if line_syllable == 3:
        word_choice = random.choice(list_of_lists1[0:1])
        if word_choice in haiku1:
            haiku1.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku1.append(word_select)
    if line_syllable == 4:
        word_choice = random.choice(list_of_lists1[0])
        if word_choice in haiku1:
            haiku1.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = word_choice
        haiku1.append(word_select)
    haikulineone = ' '.join(haiku1)
line1()


def line2():
    global haikulinetwo
    haiku2 = []
    line_syllable = 0
    if line_syllable == 0:
        word_choice = random.choice(list_of_lists2)
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        elif word_choice == syllabe5:
            line_syllable +=5     
        elif word_choice == syllabe6:
            line_syllable +=6
        elif word_choice == syllabe7:
            line_syllable +=7   
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 1:
        word_choice = random.choice(list_of_lists1[0:5])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        elif word_choice == syllabe5:
            line_syllable +=5     
        elif word_choice == syllabe6:
            line_syllable +=6
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 2:
        word_choice = random.choice(list_of_lists1[0:4])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        elif word_choice == syllabe5:
            line_syllable +=5    
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 3:
        word_choice = random.choice(list_of_lists1[0:3])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 4:
        word_choice = random.choice(list_of_lists1[0:2])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 5:
        word_choice = random.choice(list_of_lists1[0:1])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        word_select = random.choice(word_choice)
        haiku2.append(word_select)
    if line_syllable == 6:
        word_choice = random.choice(syllabe1)
        line_syllable +=1
        word_select = random.choice(word_choice)
        haiku2.append(word_choice)
    haikulinetwopreformat = ' '.join(haiku2)
    haikulinetwo = '    ' + haikulinetwopreformat
line2()

def line3():
    global haikulinethree
    haiku3 = []
    line_syllable = 0
    if line_syllable == 0:
        #while line syllable = 0: - not so elegant and would mean a LOT of lines
        word_choice = random.choice(list_of_lists1[0:4])
        if word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        elif word_choice == syllabe5:
            line_syllable +=5        
        word_select = random.choice(word_choice)
        haiku3.append(word_select)
    if line_syllable == 1:
        word_choice = random.choice(list_of_lists1[0:3])
        if word_choice in haiku3:
            haiku3.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku3.append(word_select)
    if line_syllable == 2:
        word_choice = random.choice(list_of_lists1[0:2])
        if word_choice in haiku3:
            haiku3.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku3.append(word_select)
    if line_syllable == 3:
        word_choice = random.choice(list_of_lists1[0:1])
        if word_choice in haiku3:
            haiku3.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = random.choice(word_choice)
        haiku3.append(word_select)
    if line_syllable == 4:
        word_choice = random.choice(list_of_lists1[0])
        if word_choice in haiku3:
            haiku3.append()
        elif word_choice == syllabe1:
            line_syllable +=1
        elif word_choice == syllabe2:
            line_syllable +=2
        elif word_choice == syllabe3:
            line_syllable +=3
        elif word_choice == syllabe4:
            line_syllable +=4
        word_select = word_choice
        haiku3.append(word_select)
    haikulinethree = ' '.join(haiku3)
line3()

print(haikulineone)
print(haikulinetwo)
print(haikulinethree)

completedhaiku = str(haikulineone + "\n" + haikulinetwo + "\n" + haikulinethree)

fw.write(completedhaiku)
fw.close()

print(completedhaiku)

consumer_key = "x"
consumer_secret = "x"
access_token = "x"
access_token_secret = "x"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def publictweet():

    api.update_status(completedhaiku)

publictweet()
