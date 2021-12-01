#include <stdio.h>
#include <unistd.h>
#include <random.h>
#include <limits.h>

typedef struct stack
{
    void *data;
    struct stack *next;
} stack;

void *pop(stack *s)
{
    void *data = NULL;
    if (s)
    {
        data = s->data;
        if (!s->next)
            s->data = NULL;
        else
        {
            range *tmp = s->next;
            s->data = tmp->data;
            s->next = tmp->next;
            free(tmp);
        }
    }
    return data;
}

void push(stack *s, void *data)
{
    stack *n = malloc(sizeof(stack));
    n->next = s->next;
    n->data = s->data;
    s->next = n;
    s->data = data;
}

typedef struct range
{
    int from;
    int to;
    struct range *down;
    struct range *next;
    int total;
} range;

range *head;

void track(int n)
{
    range **pp;
    range *p = head;
    range *next = NULL;
    stack s;
    s->next = NULL;
    s->data = NULL;

    push(stack, p);
    while (p) {
        if (p->from <= n && p->to >= n)
        {
            if (p->from == p->to)
            {
                p->total++;
                break;
            }
            else if (!p->down)
            {
                p->down  = malloc(sizeof(range));
                p = p->down;
                p->from = n;
                p->to = n;
                p->next = NULL;
                p->down = NULL;
                p->total = 1;
                break;
            }
            else {
                p = p->down;
            }
        }
        else if (!p->next || p->next->from > n)
        {
            range *next = p->next;
            p->next = malloc(sizeof(range));
            p = p->next;
            p->from = n;
            p->to = n;
            p->next = next;
            p->total = 1;
            break;
        }

        p = p->next;
        }
        push(stack, p);
    }

    p = pop(stack);
    while (p)
    {
        p->total++;
        p = pop(stack);
    }
}

int main(int argc, char *argv[])
{
    srand(time(NULL));
    head = malloc(sizeof(range));
    head->from = 0;
    head->to = MAX_INT;
    head->next = NULL;
    head->down = NULL;
    head->total = 0;

    int i;
    for (i=0; i < 1000; i++)
    {
        int n = rand() % 10000;
        track(rand);
    }
    return 0;
}
