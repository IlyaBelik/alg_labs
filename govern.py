from collections import defaultdict

visited_ref = 1
solved_ref = 2


def dfs(graph):
    unvisited_ref = set(graph.keys())
    progress = {}
    ordered_set = set()

    while unvisited_ref:
        for v in dfs_stack(graph, progress, unvisited_ref, unvisited_ref.pop()):
            if v in ordered_set:
                continue
            ordered_set.add(v)

            yield v


def dfs_stack(graph, progress, unvisited, first_vertex):
    stack = [first_vertex]
    while stack:
        vertex = stack.pop()
        if vertex in unvisited:
            unvisited.remove(vertex)

        if progress.get(vertex) == solved_ref:
            continue

        nearby = [edge for edge in graph[vertex] if edge not in progress]
        if nearby:
            progress[vertex] = visited_ref
            stack.append(vertex)
            stack.extend(nearby)
        else:
            progress[vertex] = solved_ref
            yield vertex


def sort(graph):
    return dfs(graph)


def read_graph(file):
    graph = defaultdict(set)
    for element in file.readlines():
        first, second = element.rstrip().split()
        graph[first].add(second)
    return graph


def main():
    with open('govern.txt') as file:
        graph = read_graph(file)

    path = sort(graph)

    result = '\n'.join(path) + '\n'

    print("Best path of getting references:")
    print(result)

    govern_out = open("govern.out", 'w')
    for res in result:
        govern_out.write(res)


if __name__ == '__main__':
    main()
