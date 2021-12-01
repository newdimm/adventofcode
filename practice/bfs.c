
struct node;
struct edge;

typedef struct node
{
	int key;
	struct edge *edges;
	struct node *next;

	struct data {
		bool visited;
	} d;
} node;

typedef struct edge
{
	node *node;
	struct edge *next;
} edge;

node *graph;

void bfs(node *g)
{

}

int main(int argc, char *argv[])
{
}
