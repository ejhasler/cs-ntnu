#include <gtkmm.h>

class NameWindow : public Gtk::Window {
public:
  Gtk::Box box;
  Gtk::Label labelFirstName;
  Gtk::Label labelLastName;
  Gtk::Entry entryFirstName;
  Gtk::Entry entryLastName;
  Gtk::Button buttonConcatenate;
  Gtk::Label labelFullName;

  NameWindow() : box(Gtk::Orientation::ORIENTATION_VERTICAL), labelFirstName("First name"), labelLastName("Last name") {
    set_title("Øving 4");

    buttonConcatenate.set_label("Combine names");
    buttonConcatenate.set_sensitive(false);

    // Pack the labels and entries into the box
    box.pack_start(labelFirstName, Gtk::PACK_SHRINK);
    box.pack_start(entryFirstName, Gtk::PACK_SHRINK);
    box.pack_start(labelLastName, Gtk::PACK_SHRINK);
    box.pack_start(entryLastName, Gtk::PACK_SHRINK);
    box.pack_start(buttonConcatenate, Gtk::PACK_SHRINK);
    box.pack_start(labelFullName, Gtk::PACK_SHRINK);

    add(box);

    entryFirstName.signal_changed().connect(sigc::mem_fun(*this, &NameWindow::on_entry_changed));
    entryLastName.signal_changed().connect(sigc::mem_fun(*this, &NameWindow::on_entry_changed));
    buttonConcatenate.signal_clicked().connect(sigc::mem_fun(*this, &NameWindow::on_button_clicked));

    show_all_children();
  }

  void on_entry_changed() {

    buttonConcatenate.set_sensitive(!entryFirstName.get_text().empty() && !entryLastName.get_text().empty());
  }

  void on_button_clicked() {

    labelFullName.set_text("Names combined: " + entryFirstName.get_text() + " " + entryLastName.get_text());
  }
};

int main(int argc, char *argv[]) {
  auto app = Gtk::Application::create(argc, argv, "org.gtkmm.example");
  NameWindow window;
  return app->run(window);
}
