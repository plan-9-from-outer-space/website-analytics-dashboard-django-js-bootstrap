
let dtOptions = {
    searchable: true,
    fixedHeight: true,
    data: {
      headings: ["Video Title", "Published Date", "Views Count"],
    },
  };
  
const dataTable = new simpleDatatables.DataTable("#datatable", dtOptions);
  
const rows = [
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Python Basic Tutorial", "16-11-2023", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
    ["Django Basic Tutorial", "16-11-2022", "72935"],
  ];
  
dataTable.insert({ data: rows });

