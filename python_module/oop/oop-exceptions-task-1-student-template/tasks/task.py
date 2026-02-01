from math import floor

class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page

    @property
    def item_count(self):
        return len(self.data)

    @property
    def page_count(self):
        num_carac = len(self.data)
        if num_carac % self.items_on_page == 0:
            return num_carac // self.items_on_page
        else:
            return num_carac // self.items_on_page + 1

    def count_items_on_page(self, page_number):
        num_paginas = self.page_count

        if page_number >= num_paginas or page_number < 0:
            raise Exception("Invalid index. Page is missing")

        if num_paginas -1 != page_number:
            return self.items_on_page

        resto = len(self.data) % self.items_on_page
        return resto if resto != 0 else self.items_on_page

    def find_page(self, data):
        match =[]
        num_paginas = self.page_count

        term_len = len(data)

        for page_number in range(num_paginas):
            start = page_number * self.items_on_page
            end = start + self.items_on_page

            # Slice extendido para cubrir palabras que empiezan en páginas anteriores
            extended_start = max(0, start - term_len + 1)
            page_text = self.data[extended_start:end]

            if data in page_text:
                match.append(page_number)

        if not match:
            raise Exception(f"'{data}' is missing on the pages'")

        return sorted(match)
    
    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start = self.items_on_page * page_number
        end = self.items_on_page * (page_number + 1)

        return self.data[start:end]


pages = Pagination('Your beautiful text', 5)

pages.page_count
# 4
pages.item_count
# 19

# pages.count_items_on_page(0)
# 5
# pages.count_items_on_page(3)
# 4
# pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.