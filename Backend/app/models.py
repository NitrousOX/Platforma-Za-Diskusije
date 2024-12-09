from datetime import datetime

class Administrator:
    def __init__(self, name, surname, address, city, country, phone, email, password, username):
        self.name = name
        self.surname = surname
        self.address = address
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.password = password
        self.username = username

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_surname(self):
        return self.surname
    def set_surname(self, surname):
        self.surname = surname
    
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city

    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password
    
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    
class User:
    def __init__(self, name, surname, address, city, country, phone, email, password, username):
        self.name = name
        self.surname = surname
        self.address = address
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.password = password
        self.username = username

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_surname(self):
        return self.surname
    def set_surname(self, surname):
        self.surname = surname
    
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city

    def get_country(self):
        return self.country
    def set_country(self, country):
        self.country = country
    
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password
    
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    
class Discussion:
    def __init__(self, title, text, author, topic):
        self.title = title
        self.text = text
        self.author = author
        self.topic = topic
        self.date_created = datetime.now()
        self.likes = 0
        self.dislikes = 0
        self.comments = []  # Lista za skladistenje komentara

        def get_title(self):
            return self.title
        def set_title(self, title):
            self.title = title

        def get_text(self):
            return self.text
        def set_text(self, text):
            self.text = text

        def get_author(self):
            return self.author
        def set_author(self, author):
            self.author = author

        def get_topic(self):
            return self.topic
        def set_topic(self, topic):
            self.topic = topic

        def get_date_created(self):
            return self.date_created
        def set_date_created(self, date_created):
            self.date_created = date_created

        def get_likes(self):
            return self.likes
        def set_likes(self, likes):
            self.likes = likes

        def get_dislikes(self):
            return self.dislikes
        def set_dislikes(self, dislikes):
            self.dislikes = dislikes

        def get_comments(self):
            return self.comments
        def set_comments(self, comments):
            self.comments = comments
            
class Comment:
    def __init__(self, text, author, discussion):
        self.text = text
        self.author = author
        self.discussion = discussion
        self.date_created = datetime.now()

    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text

    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author

    def get_discussion(self):
        return self.discussion
    def set_discussion(self, discussion):
        self.discussion = discussion

    def get_date_created(self):
        return self.date_created
    def set_date_created(self, date):
        self.date_created = date

    

    
class Topic:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.opis
    def set_description(self, description):
        self.description = description
        


class Notification:
    def __init__(self, receiver, text):
        self.receiver = receiver    #ID ili korisnicko name primaoca
        self.text = text
        self.date = datetime.now()

    def get_receiver(self):
        return self.receiver
    def set_receiver(self, receiver):
        self.receiver = receiver

    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
    
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    


