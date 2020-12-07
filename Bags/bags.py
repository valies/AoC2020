from functools import lru_cache

class FileReader():

    @classmethod
    def read_file(cls, file):
        a = []
        with open(file) as my_file:
            for line in my_file:
                a.append(line.rstrip())
        return a
        
outer_bags = []
inner_bags_counter = 0

class BagProcessing():

    @classmethod
    def form_bags_tree(cls, lines):
        bags_tree = []
        for line in lines:
            inner_bags = []
            splitted_line = line.split(" bags contain ")
            key = splitted_line[0]
            splitted_inner_bags = splitted_line[1].replace("bags", "").replace("bag", "").replace(".", "").split(",")
            for inner_bag in splitted_inner_bags:
                inner_bag = inner_bag.strip()
                bag_dictionary = {"bag": inner_bag[2:], "count": inner_bag[0]}
                inner_bags.append(bag_dictionary)
            bag_tree = {"key": key, "bags": inner_bags}
            bags_tree.append(bag_tree)
        return bags_tree

    @classmethod
    def number_of_bags_part1(cls, bags_tree):
        search_bag = "shiny gold"
        BagProcessing.process_bags_part1(search_bag, bags_tree)
        return len(set(outer_bags))

    @classmethod
    def number_of_bags_part2(cls, bags_tree):
        search_bag = "shiny gold"
        BagProcessing.process_bags_part2(search_bag, bags_tree)
        return inner_bags_counter

    @classmethod
    def process_bags_part1(cls, bag, bags_tree):
        search_bag = bag
        global outer_bags
        for bags_tree_elements in bags_tree:
            outer_bag_values = list(bags_tree_elements.values())
            for bag in outer_bag_values[1]:
                inner_bag = list(bag.values())[0]
                if search_bag == inner_bag:
                    outer_bag = list(bags_tree_elements.values())[0]
                    outer_bags.append(outer_bag)
                    BagProcessing.process_bags_part1(outer_bag, bags_tree)

    @classmethod
    def process_bags_part2(cls, bag, bags_tree):
        search_bag = bag
        global inner_bags_counter
        for bags_tree_elements in bags_tree:
            outer_bag = list(bags_tree_elements.values())[0]
            if outer_bag == search_bag:
                inner_bags = list(bags_tree_elements.values())[1]
                for inner_bag in inner_bags:
                    counter = list(inner_bag.values())[1]
                    this_bag = list(inner_bag.values())[0]
                    if this_bag != ' other' and counter != "n":
                        inner_bags_counter += int(counter)
                        for i in range(int(counter)):
                            BagProcessing.process_bags_part2(this_bag, bags_tree)

            
if __name__ == '__main__':
    lines = FileReader.read_file("bags/input.txt")
    bags_tree = BagProcessing.form_bags_tree(lines)
    print(BagProcessing.number_of_bags_part1(bags_tree))
    print(BagProcessing.number_of_bags_part2(bags_tree))
