class GildedRose(object):

    backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
    aged_brie = "Aged Brie"
    sulfuras = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def adjust_quality(self, item, value):
        item.quality = item.quality + value

    def handle_backstage_pass(self, item):
        if item.name == self.backstage_pass:
            if item.quality < 50:
                self.adjust_quality(item, 1)
            if item.sell_in < 11 and item.quality < 50:
                self.adjust_quality(item, 1)
            if item.sell_in < 6 and item.quality < 50:
                self.adjust_quality(item, 1)

            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self.adjust_quality(item, -item.quality)

    def handle_aged_brie(self, item):
        if item.name == self.aged_brie:
            if item.quality < 50:
                self.adjust_quality(item, 1)
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0 and item.quality < 50:
                self.adjust_quality(item, 1)

    def update_quality(self):
        for item in self.items:
            self.handle_backstage_pass(item)
            self.handle_aged_brie(item)
            if item.name != self.backstage_pass and item.name != self.aged_brie:
                if item.quality > 0 and item.name != self.sulfuras:
                    self.adjust_quality(item, -1)
                elif item.quality < 50:
                    self.adjust_quality(item, 1)

                if item.name != self.sulfuras:
                    item.sell_in = item.sell_in - 1

                if item.sell_in < 0 and item.quality > 0 and item.name != self.sulfuras:
                    self.adjust_quality(item, -1)
