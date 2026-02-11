from Task import Task
from B_Tree import BTree
from Segment_Tree import SegmentTree
from IntervalTree import IntervalTree

btree=BTree(2)
segmenttree=SegmentTree(1000)
intervaltree=IntervalTree()
def main():
        text=input("Command:\n")
        ar_text=text.split()
        text_func=ar_text[0]
        if text_func=="InsertTask":
            target=btree.search(int(ar_text[1]))
            if target is not None:
                print("repeated id")
            else:
                task=Task(int(ar_text[1]),int(ar_text[2]),int(ar_text[3]),int(ar_text[4]))
                bool=intervaltree.insert_task(int(ar_text[1]),int(ar_text[2]),int(ar_text[3]),int(ar_text[4]))
                if bool:
                    btree.insert(task)
                    segmenttree.insert_task(int(ar_text[1]),int(ar_text[4]))
                    print("*Inserted Successfully*")
        if text_func=="DeleteTask":
            task_id=int(ar_text[1])
            target=btree.search(task_id)
            if target is None:
                print("No Task with id:",task_id)
            else:
                btree.delete(task_id)
                segmenttree.delete_task(task_id)
                intervaltree.delete_task(task_id)
                print("*Deleted Successfully*")
        if text_func=="UpdateTask":
            target=btree.search(int(ar_text[1]))
            if target is None:
                print("No Task with id:",ar_text[1])
            else:
                btree.search_for_update(int(ar_text[1]),int(ar_text[2]),int(ar_text[3]),int(ar_text[4]))
                segmenttree.update_task(int(ar_text[1]),int(ar_text[4]))
                intervaltree.update_task(int(ar_text[1]),int(ar_text[2]),int(ar_text[3]),int(ar_text[4]))
                print("*Updated Successfully*")
        if text_func=="QueryTaskId":
            print(btree.search(int(ar_text[1]))) if btree.search(int(ar_text[1])) is not None else print("No Task with id:",ar_text[1])
        if text_func=="QueryTaskSum":
            strat_id=int(ar_text[1])
            end_id=int(ar_text[2])
            if (btree.search(strat_id) and btree.search(end_id)) is not None:
                print(segmenttree.query_task_sum(strat_id,end_id))
            else:
                print("Invalid Id!!!!")     
        if text_func=="PrintTrees":
            print("BTree:")
            btree.print_tree()
            print("------------------------------------------------------")
            print("Segment Tree:")
            segmenttree.print_tree()
            print("------------------------------------------------------")
            print("Interval Tree:")
            intervaltree.print_tree()
            print("------------------------------------------------------")
        if text_func=="Quit":
            print("Have a Good Time ;)")
            exit()
        else:
            print("Invalid request")
while True:
    try:
        main()
    except ValueError:
        print("Invalid input!! (Enter Number)")
        continue
    except SyntaxError:
        break