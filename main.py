from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random

AD_SERVERS = {
    "googleads.g.doubleclick.net",
    "ads.facebook.com",
    "graph.facebook.com",
    "app-measurement.com",
    "ads.mopub.com",
    "ads.twitter.com",
    "pagead2.googlesyndication.com",
    "ads.inmobi.com",
    "ads.yahoo.com",
    "tracking.adjust.com",
    "ads.pubmatic.com",
    "ads.vungle.com"
}

class AdBlockEngine:
    def __init__(self):
        self.blocked = 0
        self.trackers = 0
        self.saved = 0
        self.last = "None"

    def check(self, domain):
        if domain in AD_SERVERS:
            self.blocked += 1
            self.trackers += 1
            self.saved += 120
            self.last = domain

engine = AdBlockEngine()

FAKE = list(AD_SERVERS) + [
    "google.com", "github.com", "wikipedia.org"
]

class SlayerAdBlocker(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.title = Label(
            text="[b][color=00ff00]Slayer Ad-Blocker[/color][/b]",
            markup=True,
            font_size="26sp"
        )

        self.stats = Label(font_size="16sp")
        box.add_widget(self.title)
        box.add_widget(self.stats)

        Clock.schedule_interval(self.tick, 1)
        return box

    def tick(self, dt):
        engine.check(random.choice(FAKE))
        self.stats.text = (
            f"🚫 Ads Blocked: {engine.blocked}\n"
            f"🕵️ Trackers: {engine.trackers}\n"
            f"💾 Data Saved: {engine.saved} KB\n"
            f"🌐 Last Source:\n{engine.last}"
        )

SlayerAdBlocker().run()
