
int is_a_solution(int a[],int k, data input)
{
    return k==input;
}

void construct_candidates(int a[],int k, data input, int c[],int *ncandidates) 
{
    c[0] = 1;
    c[1] = 0;
    *ncandidates = 2;
}

void process_solution(int a[],int k,data input)
{
    int i;
    printf("{");
    for(i=1;i<=k;i++)
        if(a[i])
            printf(" %d",i);
    printf(" }\n");
}
bool finished = FALSE; /* 是否获得全部解? */
backtrack(int a[], int k, data input)
{
    int c[MAXCANDIDATES]; /*这次搜索的候选 */
    int ncandidates;      /* 候选数目 */
    int i;                /* counter */
    if (is_a_solution(a, k, input))
        process_solution(a, k, input);
    else
    {
        k = k + 1;
        construct_candidates(a, k, input, c, &ncandidates);
        for (i = 0; i < ncandidates; i++)
        {
            a[k] = c[i];
            make_move(a, k, input);
            backtrack(a, k, input);
            unmake_move(a, k, input);
            if (finished)
                return; /* 如果符合终止条件就提前退出 */
        }
    }
}
generate_subsets(int n)
{
　　int a[NMAX];
　　backtrack(a,0,n);
}