from tools.connectMDB import get_by_ID
from tools.connectMDB import get_one_by_ID
from tools.connectMDB import get_collection

class message(object):

    def __init__(self,id):
        #define all time-dependent attributes with timestamp
        entries = get_by_ID(id)
        self.quote_count = {}
        self.retweet_count = {}
        self.favorite_count = {}
        self.reply_count = {}
        for singleEntry in entries:
            self.quote_count[singleEntry['timestamp_ms']] = singleEntry['quote_count']
            self.retweet_count[singleEntry['timestamp_ms']] = singleEntry['retweet_count']
            self.favorite_count[singleEntry['timestamp_ms']] = singleEntry['favorite_count']
            self.reply_count[singleEntry['timestamp_ms']] = singleEntry['reply_count']

        #define all other attributes
        entry = get_one_by_ID(id)
        self.text = entry['text']
        self.created_at = entry['created_at']
        self.id = entry['id']
        self.id_str = entry['id_str']
        self.source = entry['source']
        self.truncated = entry['truncated']
        self.in_reply_to_status_id = entry['in_reply_to_status_id']
        self.in_reply_to_status_id_str = entry['in_reply_to_status_id_str']
        self.in_reply_to_user_id = entry['in_reply_to_user_id']
        self.in_reply_to_user_id_str = entry['in_reply_to_user_id_str']
        self.in_reply_to_screen_name = entry['in_reply_to_screen_name']
        self.user = entry['user']
        self.geo = entry['geo']
        self.coordinates = entry['coordinates']
        self.place = entry['place']
        self.contributors = entry['contributors']
        self.is_quote_status = entry['is_quote_status']

    def get_text(self):
        return self.text,self.text.split(),self.text.split().__len__()


def get_array_of_words(len = 10,CLEAN = True):
    messages = []
    clean = []
    i = 0
    if CLEAN ==True:
        for entry in get_collection().find():
            m = message(entry["id"])
            clean.extend(get_clean_text(m))
            messages.append(message)
            i = i+1
            print(i)
            if i >len:
                break
    else:
        for entry in get_collection().find():
            m = message(entry["id"])
            __,arr,__ =m.get_text()
            clean.extend(arr)
            messages.append(message)
            i = i +1
            if i >len:
                break
    return clean,messages


def get_clean_text(message = message, options=['www','https']):
    __,arr,__ = message.get_text()
    for opt in options:
        for word in arr:
            if opt in word:
                arr.remove(word)
    return arr



if __name__ == "__main__":
    # 9.967880685930947e+17 is the ID of the first entry in the Dataset
    m = message(9.967880685930947e+17)

    for key in m.quote_count.keys():
        print("Timestamp in ms: " + key + "  |  No. of quotes: " + str(m.quote_count[key]))