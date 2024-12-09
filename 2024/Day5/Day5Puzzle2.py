with open('Day5InputPart1.txt') as file:
        rules_text = file.read().splitlines()

with open('Day5InputPart2.txt') as file:
        updates = file.read().splitlines()


rules = []
test = [1,2,3]
result = 0


def get_middle(array):
        return array[int(len(array)/2)] 



def get_page_rules(page):
        out_rules = []
        for rule in rules:
                if rule[0] == page:
                        out_rules.append(rule[1])
        return out_rules


def is_update_valid(pages):
        pages_to_test = pages.copy()
        passed_pages = []

        for page in reversed(pages):
                pages_to_test.remove(page)
                page_rules = get_page_rules(page)

                for previous_page in pages_to_test:
                        if previous_page in page_rules:
                                return False

        return True




def page_is_valid_earlier(page_to_add, previous_page):
        
        rules = get_page_rules(previous_page)

        pass


def reorder_pages(pages):
        ordered_pages = []

        for page in pages:

                for x_page in ordered_pages:
                        if page_is_valid_earlier:
                                pass
                        else:
                                pass

        return ordered_pages

               


for value in rules_text:
        rules.append(value.split("|"))

for pages in updates:
        pages = pages.split(",")
        if is_update_valid(pages):
                result += int(get_middle(pages))
        else:
                pages = reorder_pages(pages)

print(result)

