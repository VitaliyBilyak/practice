from datetime import date
from django.shortcuts import render

all_posts=[
    {
        "slug":"a_day_in_the_life_of_our_dobermans",
        "image":"doberman.jpg",
        "author":"Vitalik",
        "date": date(2024, 5 ,21),
        "title": "A Day in the Life of Our Dobermans",
        "excerpt":"Discover what a typical day looks like with our Dobermans, from morning walks to playtime and training sessions.",
        "content": """ 
            Curious about what a day with our Dobermans is like? Here's a glimpse into their daily routine! Each day starts with an energetic morning walk, followed by breakfast and some playtime in the yard. Our Dobermans love to run around and chase their favorite toys.
            
            After a good play session, it's time for some training. We work on basic commands and tricks, which they pick up quickly thanks to their intelligence and enthusiasm. Midday is usually reserved for relaxation and naps, as our Dobermans need their rest to stay active and happy.
           
            In the afternoon, we enjoy another walk or a fun outing to a nearby park. The day ends with dinner and some quality time with the family. We're thrilled with how well they're adjusting and can't wait for the many adventures ahead.
            
            Stay tuned for more updates on our Dobermans' daily life and their ongoing training progress!
        """,
    },
    {
        "slug":"Our_new_family",
        "image":"dobi.jpg",
        "author":"Vitalik",
        "date": date(2021, 7 ,21),
        "title": "Our new family: Two Dobermans!",
        "excerpt":"We are happy to share the great news - we have bought two Dobermans! One boy and one girl have already become favorites in our family.",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        """,
    },
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Vitalik",
        "date": date(2021, 7 ,21),
        "title": "Mountain Miking",
        "excerpt":"There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the views",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

        """,
    },
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "all-posts.html",{
    "all_posts": all_posts
    })

def post_datail(request, slug):
    indentified_post= next(post for post in all_posts if post['slug'] == slug)
    return render(request, "post-detail.html" ,{
        "post": indentified_post
    })
