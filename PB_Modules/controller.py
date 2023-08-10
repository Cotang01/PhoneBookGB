import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.book_loaded)
            case 2:
                model.save_pb()
                view.print_info(txt.book_saved)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.not_loaded_pb)
            case 4:
                new_user = view.new_user()
                model.add_contact(new_user)
                view.print_info(txt.user_added)
            case 5:
                search_user = view.find_contact()
                found_user = model.user_search(search_user)
                view.found_contact(found_user)
                view.print_info(txt.user_found)
            case 6:
                user_change = view.change_contact()
                info_change = view.additional_change_info()
                model.data_change(user_change, info_change)
                view.print_info(txt.user_changed)
            case 7:
                user_delete = view.user_to_delete()
                model.deleting_user(user_delete)
                view.print_info(txt.user_deleted)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.confirm_changes):
                        model.save_pb()
                view.print_info(txt.exit_pb)
                exit()
            case _:  # Как else
                pass
