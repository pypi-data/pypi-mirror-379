from mahamm_sadeh_iythar.cli import add_task, show_tasks, mark_done, delete_task, tasks

def test_add_and_show(capsys):
    tasks.clear()
    add_task("Buy milk")
    assert len(tasks) == 1
    show_tasks()
    captured = capsys.readouterr()
    assert "Buy milk" in captured.out

def test_mark_and_delete(capsys):
    tasks.clear()
    add_task("Test task")
    mark_done(0)
    assert tasks[0]["done"] is True
    delete_task(0)
    assert tasks == []
