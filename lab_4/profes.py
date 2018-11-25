import math


def DFS_params(graph, first, first_w, difference):
    edges = {first_w}

    def DFS(first):
        passed.add(first)
        for i, weight in enumerate(graph[first]):
            if i not in passed and i != first:
                edges.add(weight)
                if (max(edges) - min(edges)) <= difference:
                    DFS(i)
                else:
                    edges.remove(weight)

    passed = set()
    DFS(first)
    return passed


def reversed_data(graph, n):
    processed_graph = [[0 for i in range(n)] for i in range(n)]
    for vertex in range(n):
        for second_vertex in range(n):
            processed_graph[vertex][second_vertex] = graph[second_vertex][vertex]
    return processed_graph


def drunk_professors(graph, reversed_data, N, difference):
    statement = set()
    statement_found = False
    for difference in range(difference):
        second_graph = graph[0].copy()[1:]
        for start_weight in second_graph:
            answer = DFS_params(graph, 0, start_weight, difference)
            if len(answer) == N:
                reverse_statement = DFS_params(reversed_data, 0, start_weight, difference)
                if len(reverse_statement) == N:
                    statement.add(difference)
                    statement_found = True
            if statement_found:
                break
        if statement_found:
            break
    print("Difference between statements: " + str(statement))
    profes = open("out.txt", 'w')
    for stat in statement:
        profes.write(str(stat) + "\n")


if __name__ == "__main__":
    for line in open("in.txt"):
        numbers = line.split(",")
    output = []
    for v in numbers:
        output.append(int(v))
    N = int(math.sqrt(len(numbers)))

    graph = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = output[i * N + j]
    print("Professors' statements are : " + str(graph) + "\n")

    values = set(output)
    N = len(graph)
    reversed_graph = reversed_data(graph, N)

    max_edge = max(values)
    min_edge = min(values)

    max_difference = max_edge - min_edge + 1
    drunk_professors(graph, reversed_graph, N, max_difference)
