/*
nbtutor - a small utility to indicate which cells should be cleared (exercises).

Mainly adapated from the example in Jonathan Frederic his tutorial
(https://blog.safaribooksonline.com/2013/12/18/ipython-notebook-plugins/)

*/

console.log("Start loading nbtutor");

// Create and register the method that creates the checkbox that
// alters the new 'exclude'
// flag of the cell's metadata.
var flag_name = 'clear_cell';
var cell_flag_init = IPython.CellToolbar.utils.checkbox_ui_generator(

    // Name
    flag_name,

    // Setter, called when the checkboxes state has been changed.
    // Sets the flag name and
    // value in the cell's metadata.
    function(cell, value){
        cell.metadata[flag_name] = value;
    },

    // Getter, called when the control is rendered.  Determines the initial
    // state of the checkbox.  If the flag doesn't in the metadata, default
    // to false.
    function(cell){
        if (cell.metadata[flag_name] === undefined || cell.metadata[flag_name]
           == false) {
            return false;
        } else {
            return true;
        }
    }
);
IPython.CellToolbar.register_callback(flag_name, cell_flag_init);

// Create and register the toolbar with IPython.
IPython.CellToolbar.register_preset('Nbtutor - export exercises', [flag_name]);

console.log("Our extension was loaded successfully");
