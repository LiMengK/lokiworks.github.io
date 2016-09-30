---
layout: post
title: 算法设计-最大流之push-relabel
keywords:
  - push-relabel

description: 学习最大流之push-relabel算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.伪代码:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_pushrelabel_maxflow_code01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_pushrelabel_maxflow_code02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160930_pushrelabel_maxflow_code03.PNG)
### 2.代码片段:
```
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;


struct  Edge
{
    /// <summary>
    /// To store current flow and capacity of edge.
    /// </summary>
    int flow;
    int capacity;

    /// <summary>
    /// An edge u-->v has start vertext as u and end vertext as v.
    /// </summary>
    int u;
    int v;

    Edge(int flow, int capacity, int u, int v)
    {
        this->flow = flow;
        this->capacity = capacity;
        this->u = u;
        this->v = v;
    }
};

/// <summary>
/// Represent a vertex
/// </summary>
struct Vertex
{
    int h;
    int excessFlow;

    Vertex(int h, int excessFlow)
    {
        this->h = h;
        this->excessFlow = excessFlow;
    }
};

class Graph
{
public:
    /// <summary>
    /// Constructor
    /// </summary>
    Graph(int V)
    {
        this->V = V;
        for (int i = 0; i < V; ++i)
        {
            ver.push_back(Vertex(0, 0));
        }
    }
    /// <summary>
    /// add edge to graph
    /// </summary>
    void AddEdge(int u, int v, int capacity)
    {
        edge.push_back(Edge(0, capacity, u, v));
    }
    /// <summary>
    /// get maximum flow from s to t
    /// </summary>
    int GetMaxFlow(int s, int t)
    {
        Preflow(s);

        // loop untill none of the Vertex is in overflow
        int u = OverFlowVertex(ver);
        while (u != -1)
        {
            if (!Push(u))
            {
                Relabel(u);
            }
            u = OverFlowVertex(ver);
        }

        return ver.back().excessFlow;
    }

private:
    /// <summary>
    /// No. of vertexes
    /// </summary>
    int V;

    vector<Vertex> ver;
    vector<Edge> edge;

    /// <summary>
    /// push excess flow from u
    /// </summary>
    bool Push(int u)
    {
        // Traverse through all edges to find an adjacent (of u)
        // to which flow can be pushed
        for (int i = 0; i < edge.size(); ++i)
        {
            // Checks u of current edge is same as given
            // overflowing vertex
            if (edge[i].u == u)
            {
                // flow should be less to capacity
                if (edge[i].flow < edge[i].capacity)
                {
                    // push is only possible if height of adjacent
                    // is smaller than height of overlflowing vertex
                    if (ver[u].h > ver[edge[i].v].h)
                    {
                        // Flow to be pushed is equal to minimum of
                        // remaining flow to on edge and excess flow.
                        int flow = std::min(edge[i].capacity - edge[i].flow, ver[u].excessFlow);

                        // reduce excess flow for overflowing vertex
                        ver[u].excessFlow -= flow;
                        // increase excess flow for adjacent
                        ver[edge[i].v].excessFlow += flow;
                        // add residual flow
                        edge[i].flow += flow;

                        UpdateReverseEdgeFlow(i, flow);
                        return true;
                    }
                }


            }
        }

        return false;
    }

    /// <summary>
    /// relabel a vertex u
    /// </summary>
    void Relabel(int u)
    {
        // Initialize minimum height of an adjacent
        int mh = std::numeric_limits<int>::max();

        // Find the adjacent with minimum height
        for (int i = 0; i < edge.size(); ++i)
        {
            if (edge[i].u == u)
            {
                if (edge[i].flow < edge[i].capacity)
                {
                    if (ver[edge[i].v].h < mh)
                    {
                        mh = ver[edge[i].v].h;
                        // updating hegiht of u
                        ver[u].h = mh + 1;
                    }
                }
            }
        }
    }

    int OverFlowVertex(const vector<Vertex> & ver)
    {
        for (int i = 1; i < ver.size() - 1; ++i)
        {
            if (ver[i].excessFlow > 0)
            {
                return i;
            }
        }
        // -1 if no overflowing vertex
        return -1;
    }

    /// <summary>
    /// initialize preflow
    /// </summary>
    void Preflow(int s)
    {
        // Making h of source vertex equal to no. of vertices
        // Height of other vertices is 0
        ver[s].h = ver.size();

        for (int i = 0; i < edge.size(); ++i)
        {
            // if current edge goes from source
            if (edge[i].u == s)
            {
                // flow is equal to capacity
                edge[i].flow = edge[i].capacity;
                // Initialize excess flow for adjacent v
                ver[edge[i].v].excessFlow += edge[i].flow;
                // Add an edge from v to s in residual graph with 
                // capacity equal to 0
                edge.push_back(Edge(-edge[i].flow, 0, edge[i].v, s));

            }
        }
    }

    void UpdateReverseEdgeFlow(int i, int flow)
    {
        int u = edge[i].v;
        int v = edge[i].u;

        for (int j = 0; j < edge.size(); ++j)
        {
            if (edge[j].v == v && edge[j].u == u)
            {
                edge[j].flow -= flow;
                return;
            }
        }

        // add reverse edge in residual graph
        Edge e = Edge(0, flow, u, v);
        edge.push_back(e);
    }

};



int main()
{

    int V = 6;
    Graph g(V);

    // Creating above shown flow network
    g.AddEdge(0, 1, 16);
    g.AddEdge(0, 2, 13);
    g.AddEdge(1, 2, 10);
    g.AddEdge(2, 1, 4);
    g.AddEdge(1, 3, 12);
    g.AddEdge(2, 4, 14);
    g.AddEdge(3, 2, 9);
    g.AddEdge(3, 5, 20);
    g.AddEdge(4, 3, 7);
    g.AddEdge(4, 5, 4);

    // Initialize source and sink
    int s = 0, t = 5;

    cout << "Maximum flow is " << g.GetMaxFlow(s, t);
    return 0;
}


```
