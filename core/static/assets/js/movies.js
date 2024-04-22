
let dtOptions = {
    searchable: true,
    fixedHeight: true,
    data: {
      headings: ["id", "title", "year", "rating", "votes"],
    },
  };

const dataTable = new simpleDatatables.DataTable("#datatable", dtOptions);
  
fetch('/api/movies-with-ratings')
    .then (res => res.json())
    .then (data => { 
        dataTable.insert({data: data.data});
    });

