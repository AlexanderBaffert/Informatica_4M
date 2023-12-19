#Baffert Alexander 4M^
#class and inheritance
class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.friends_list = []

    def add_friend(self, friend):
        self.friends_list.append(friend)

    def remove_friend(self, friend):
        self.friends_list.remove(friend)

    def post_content(self, content):
        return Post(content)
    def __str__(self):
        return f"User {self.username} has {len(self.friends_list)} friends"

class RegularUser(User):
    def __init__(self, user_id, username, email, password, interests):
        super().__init__(user_id, username, email, password)
        self.interests = interests
        self.activity_log = []

    def like_post(self, post):
        post.like()

    def comment_on_post(self, post, comment):
        post.comment(comment)

class BusinessUser(User):
    def __init__(self, user_id, username, email, password, business_id, products):
        super().__init__(user_id, username, email, password)
        self.business_id = business_id
        self.products = products
        self.customer_reviews = []

    def advertise(self):
        return f"Advertise {self.business_id}"

    def respond_to_reviews(self, review):
        self.customer_reviews.append(review)

class Post:
    def __init__(self, post_id, content, timestamp):
        self.post_id = post_id
        self.content = content
        self.timestamp = timestamp
        self.comments = []
        self.likes = 0

    def like(self):
        self.likes += 1
        return print(f"Total likes: {self.likes}")

    def comment(self, comment):
        self.comments.append(comment)

    def share(self):
        return f"Share {self.post_id}"

class TextPost(Post):
    def __init__(self, post_id, content, timestamp, word_count, language):
        super().__init__(post_id, content, timestamp)
        self.word_count = word_count
        self.language = language

    def analyze_sentiment(self):
        return print(f"Analyze sentiment of {self.post_id}")

class ImagePost(Post):
    def __init__(self, post_id, content, timestamp, image_url, resolution):
        super().__init__(post_id, content, timestamp)
        self.image_url = image_url
        self.resolution = resolution

    def apply_filter(self, filter):
        return print(f"Apply {filter} filter to {self.post_id}")

    def tag_people(self, people):
        return print(f"Tag {people} in {self.post_id}")

#main
#users
user1 = User(1, "user1", "", "")
user2 = RegularUser(2, "user2", "", "", ["sports", "music"])
user3= BusinessUser(3, "user3", "", "", "business1", ["product1", "product2"])
for i in range(4):
    user1.add_friend(user2)
print(user1.__str__())
user2.like_post(Post(1, "content", "timestamp"))
user2.comment_on_post(Post(2, "content", "timestamp"), "comment")
user2.like_post(Post(1, "content", "timestamp"))
#posts
post = Post("1", "content", "timestamp")
for i in range(4):
    user2.like_post(post)
post.like()
#different types of posts
text_post = TextPost("1", "content", "timestamp", 100, "english")
image_post = ImagePost("2", "content", "timestamp", "image_url", "resolution")
text_post.analyze_sentiment()
image_post.apply_filter("filter")