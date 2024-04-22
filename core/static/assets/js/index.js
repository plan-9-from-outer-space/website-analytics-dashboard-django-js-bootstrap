const totalViewChart = document.getElementById("total-views-chart");
const revenueChart = document.getElementById("revenue-chart");
const subscriberCountChart = document.getElementById("subscriber-count-chart");
const trafficSourcesChart = document.getElementById("traffic-sources-chart");

let myDatatable = document.getElementById("datatable");
// const datatable = document.getElementById("datatable");

const labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"];
const data = [65, 59, 80, 81, 56, 55, 40];
const trafficSourceLabels = ["YouTube", "Facebook", "Dummy", "Snapchat", "Google", "Firefox", "Opera"];

// Fetch the total-views data
fetch('/api/total-views')
    .then (res => res.json())
    .then (data => {
        new Chart(totalViewChart, {
          type: "line",
          data: {
            labels: data.labels,
            datasets: [
              {
                label: "Views",
                data: data.data,
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              y: {
                beginAtZero: false,
              },
            },
          },
        });
      });

new Chart(revenueChart, {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Revenue",
        data: data,
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

new Chart(subscriberCountChart, {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Subscriber Count",
        data: data,
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

new Chart(trafficSourcesChart, {
  type: "pie",
  data: {
    labels: trafficSourceLabels,
    datasets: [
      {
        label: "Share",
        data: data,
        borderWidth: 1,
      },
    ],
  },
  // options: {
  //   scales: {
  //     y: {
  //       beginAtZero: true,
  // }}}
});

// const testRows = [
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Python Basic Tutorial", "16-11-2023", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
//   ["Django Basic Tutorial", "16-11-2022", "72935"],
// ];

// fetch('/api/total-views')
//     .then (res => res.json())
//     .then (data => {
//         new Chart(totalViewChart, { ... }));

let dtOptions = {
  searchable: true,
  fixedHeight: true,
  data: {
    headings: ["Video Title", "Published Date", "Views Count"],
  },
};

// const myDatatable = document.getElementById("datatable");  // at top of file

let dataTable = new simpleDatatables.DataTable(myDatatable, dtOptions);

// let myTable = document.querySelector("#myTable");
// let dataTable = new DataTable(myTable);
// or
// let dataTable = new DataTable("#myTable");

fetch('/api/datatable')
    .then (res => res.json())
    .then (data => { 
        // console.log(data.data);
        dataTable.insert({data: data.data});
        // dataTable.insert({data: testRows});
    });

