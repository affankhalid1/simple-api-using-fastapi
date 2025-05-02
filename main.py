from fastapi import FastAPI , HTTPException
import random
import string

app = FastAPI()


motivational_money_quotes = [
    "Don't stay broke just to look rich. Build real wealth in silence.",
    "The best way to predict your future is to create it — with hustle and money moves.",
    "Chase freedom, not just paychecks.",
    "Money flows to those who take action, not those who wait.",
    "Wake up with determination, grind with purpose, and earn with pride.",
    "You’re only one skill, one hustle, one idea away from changing your life.",
    "Make money work for you while you sleep — that's the real flex.",
    "The grind will pay you more than luck ever could.",
    "Broke is temporary. Hustle is forever.",
    "You don’t need more time, you need more focus.",
    "Your salary is the seed — how you plant it decides your future.",
    "Money earned through value lasts longer than money chased through shortcuts.",
    "The road to wealth is paved with action, not intention.",
    "Success loves speed. Start before you're ready.",
    "Discipline creates freedom — financial and personal.",
    "A side hustle today is financial freedom tomorrow.",
    "No one is coming to rescue your bank account. It’s all on you.",
    "Earn like you’re broke. Invest like you’re wealthy.",
    "Be obsessed with building income streams, not just spending streams.",
    "Your excuses are more expensive than your goals.",
    "Invest in your skills. They print the money.",
    "The grind doesn’t stop until your bank account looks like a phone number.",
    "Money loves clarity. Know what you want and go for it.",
    "Hard work beats talent when talent doesn’t hustle.",
    "You can either watch Netflix or your net worth grow — pick one.",
    "Consistency builds cash flow.",
    "Don’t wait for the perfect moment. Start now, learn as you earn.",
    "The earlier you start earning smart, the earlier you stop working hard.",
    "Hustle until your haters ask if you’re hiring.",
    "Earn money in silence. Let success make the noise.",
    "If you don’t build your dream, someone will hire you to build theirs.",
    "Money doesn’t sleep — and neither does real ambition.",
    "Every dollar you earn can be your employee — make them work.",
    "Create before you consume. That’s how wealth is built.",
    "Turn your passion into profit, and your energy into income.",
    "Make your side hustle your main hustle — then scale it.",
    "Money is a reflection of the value you provide. Increase your value.",
    "Success is rented, and rent is due every day — pay up in hustle.",
    "Get so financially secure that you forget it's payday.",
    "Don't downgrade your dreams to match your income. Upgrade your hustle.",
    "Your grind determines your lifestyle.",
    "You don’t get rich by working 9 to 5 — you get rich by working 5 to 9.",
    "Smart work creates shortcuts that hard work never finds.",
    "Create something once that pays you forever.",
    "The rich build assets. The poor buy liabilities.",
    "You can have results or excuses. Not both.",
    "Money is a result, not a goal. Focus on creating value.",
    "Millionaires aren’t lucky — they’re intentional.",
    "Your income grows when your mindset does.",
    "A broke mindset can’t make rich money.",
    "The rich hustle for assets. The broke hustle for paychecks.",
    "Surround yourself with people who talk goals, not gossip.",
    "Invest your time before you invest your money.",
    "Your energy is currency. Spend it wisely.",
    "There’s no elevator to wealth — only stairs and sweat.",
    "Earn while they sleep. Grind while they party. Live how they dream.",
    "If you want to be rich, solve bigger problems.",
    "Make your habits richer than your taste.",
    "Get rich in value. Money will follow.",
    "Poor habits create poor results. Rich habits build empires.",
    "Your mindset is your money magnet.",
    "Small daily actions create massive financial change.",
    "Let your hustle make noise before your lifestyle does.",
    "If it doesn’t make money, make it make sense.",
    "Don’t get distracted by lifestyle. Stay focused on building income.",
    "Learn, earn, repeat. That’s the money cycle.",
    "Every millionaire was once broke with a plan.",
    "Stop scrolling. Start building.",
    "Don’t chase money. Chase skills — money follows.",
    "Money isn’t everything, but not having it can hold you back from everything.",
    "Make money a tool, not your master.",
    "Act broke, stack money, stay silent, build legacy.",
    "Your hustle determines your harvest.",
    "Don't sleep on your talent — it’s your ticket to income.",
    "Passive income is the goal. Active hustle is the path.",
    "One idea. One execution. That’s all it takes.",
    "If you’re not building wealth, you’re working for someone who is.",
    "Earn more, spend less, invest the difference.",
    "Work until your signature becomes an autograph.",
    "Hustle like no one’s watching. One day everyone will.",
    "Your first $100 is the hardest. After that, it’s systems.",
    "Build your skills until they pay your bills.",
    "Dream big, hustle smart, earn always.",
    "Money is freedom. Freedom is priceless.",
    "Skip the drama. Stack the commas.",
    "Every second spent doubting is a second wasted not earning.",
    "Discipline now creates freedom later.",
    "Your future self will thank you for the hustle today.",
    "Don’t flex what you haven’t earned yet. Build first.",
    "Start broke. Stay hungry. Finish wealthy.",
    "Get uncomfortable. That's where the money is.",
    "Multiple income streams = multiple options.",
    "Risk is scary, but regret is worse.",
    "Start small. Think big. Scale fast.",
    "More value = more money. Focus there.",
    "Stop chasing money. Attract it with skill and service.",
    "Your hustle is louder than your words.",
    "Money earned through passion lasts longer.",
    "Focus on progress, not perfection — it still pays.",
    "Don’t fear the grind. Fear being stuck.",
    "Discipline creates dollars.",
    "Your bank account reflects your daily habits.",
    "Think big. Act bold. Earn relentlessly."
]


side_hustles = [
    "Freelance Graphic Design",
    "Web Development",
    "Video Editing",
    "Copywriting",
    "Virtual Assistant",
    "Online Tutoring",
    "Resume/CV Writing",
    "SEO Consultant",
    "Social Media Manager",
    "UX/UI Design",
    "Print-on-Demand Store",
    "Dropshipping",
    "Selling Digital Products",
    "Reselling on Amazon or eBay",
    "Create & Sell Art Prints",
    "Handmade Crafts",
    "Subscription Box Business",
    "3D Printing Services",
    "Buy & Flip Phones or Tech",
    "Custom Perfume or Cosmetic Kits",
    "Pet Sitting or Dog Walking",
    "House Cleaning Service",
    "Mobile Car Wash & Detailing",
    "Photography/Videography",
    "Fitness Trainer",
    "Home Tutoring",
    "Gardening/Landscaping",
    "Errand Running or Personal Shopper",
    "Laundry & Ironing Service",
    "Furniture Assembly & Handyman Work",
    "Prompt Engineering Services",
    "AI-Generated Content Creation",
    "Build AI Tools or SaaS Apps",
    "No-Code App Development",
    "Data Annotation Jobs",
    "Voiceover with AI Tools",
    "AI Avatar Creation for Businesses",
    "AI-Enhanced YouTube Channel",
    "Develop Chrome Extensions",
    "Niche Affiliate AI Website",
    "YouTube Automation Channel",
    "Podcasting",
    "Substack or Newsletter",
    "TikTok Influencer in a Micro-Niche",
    "Instagram Theme Page",
    "Live Streaming (Gaming, Study, or Chat)",
    "Course Creation",
    "Voice Acting for Audiobooks or Characters",
    "OnlyFans/Patreon-Style Content (Non-Adult)",
    "Start a Paid Community or Discord"
]
api_key_ = ''.join(random.choices(string.ascii_letters + string.digits, k=16) )


@app.get("/")
def root():
    return f"Hello Guys, If you want to get side hustle ideas go to /side_hustles or if you want motivational quote for to earn money so you have to go to /money_quotes."

@app.get("/side_hustles")
def get_side_hustles(api_key:str):
    if api_key != api_key_:
        raise HTTPException(status_code=401, detail = "Invalid APi Key")
    """Returns a random side hustle idea"""
    return f"side_hustle: {random.choice(side_hustles)}"

@app.get("/money_quotes")
def get_money_quotes(api_key:str):
    if api_key != api_key_:
        raise HTTPException(status_code=401, detail = "Invalid APi Key")
    """Returns a motivational Money quotes"""
    return f"money_quote: {random.choice(motivational_money_quotes)}"

@app.get("/get_api_key")
def get_api_key():
    """Temporary route to see the current key (not for production)"""
    return f"your api key: {api_key_}"