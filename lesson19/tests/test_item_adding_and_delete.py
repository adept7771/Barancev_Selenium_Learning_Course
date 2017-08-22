from nose.tools import assert_true


def test_item_adding_and_delete(app):

    app.add_new_item_to_cart(5)
    app.delete_all_items_in_cart()




