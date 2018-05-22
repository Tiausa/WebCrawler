
//create somewhere to put the force directed graph
var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var radius = 15;

//var obj = JSON.parse('{ "URLs": {"www.google.com": {"edges": ["www.zzz.com"], "found": false, "title": "title0"}, "www.zzz.com": { "edges": [], "found": false, "title": "title1" }}, "cookie": "graph 3", "start": "0"}');
//var obj = JSON.parse('{"start": "0", "cookie": "test7903", "URLs": {"0": {"found": false, "edges": ["1"], "title": "title0"}, "1": {"found": false, "edges": ["0"], "title": "title1"}, "2": {"found": false, "edges": ["0"], "title": "title2"}, "3": {"found": false, "edges": ["2", "1"], "title": "title3"}, "4": {"found": false, "edges": [], "title": "title4"}}}');
var obj = JSON.parse(document.getElementById("script").getAttribute("jsonObj"));

urls = Object.keys(obj["URLs"]);

console.log(urls);

var nodes = [
],
	lastNodeId = 0,
	links = [
	];

for (var x = 0; x < urls.length; x++) {
    var i = { id: urls[x], reflexive: false, keyword: obj['URLs'][urls[x]]['found'], title: obj['URLs'][urls[x]]['title'] };
    if (x != 0) {
        i["reflexive"] = true;
    }

    nodes.push(i);
    console.log(nodes);
}

for (var i = 0; i < urls.length; i++) {
    for (var j = 0; j < obj["URLs"][urls[i]]["edges"].length; j++) {
        var y = urls.indexOf(obj["URLs"][urls[i]]["edges"][j]);
        console.log(y);

        var k = {
            source: nodes[i], target: nodes[y], left: false, right: true
        };
        links.push(k);
        console.log(links);
        console.log(k);
    }
}

//set up the simulation and add forces  
var simulation = d3.forceSimulation()
					.nodes(nodes);

var link_force = d3.forceLink(links)
                        .id(function (d) { return d.name; });

var charge_force = d3.forceManyBody()
    .strength(-5000);

var center_force = d3.forceCenter(width / 2, height / 2);

simulation
    .force("charge_force", charge_force)
    .force("center_force", center_force)
    .force("links", link_force)
;

// define arrow markers for graph links
svg.append("defs").append("marker")
    .attr("id", "end-arrow")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 19)
    .attr("refY", 0)
    .attr("markerWidth", 8)
    .attr("markerHeight", 8)
    .attr("orient", "auto")
  .append("svg:path")
    .attr("d", "M0,-5L10,0L0,5");

svg.append("defs").append("marker")
    .attr("id", "start-arrow")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", -9)
    .attr("refY", 0)
    .attr("markerWidth", 8)
    .attr("markerHeight", 8)
    .attr("orient", "auto")
  .append("svg:path")
    .attr("d", "M10,-5L0,0L10,5");

//add tick instructions: 
simulation.on("tick", tickActions);

//add encompassing group for the zoom 
var g = svg.append("g")
    .attr("class", "everything");

//draw lines for the links 
var link = g.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", 2)
      .attr("marker-start", function (d) { return d.left ? "url(#start-arrow)" : ''; })
      .attr("marker-end", function (d) { return d.right ? "url(#end-arrow)" : ''; })
      .style("stroke", linkColour);


//draw circles for the nodes 
var node = g.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")
        .attr("r", radius)
        .attr("fill", circleColour);


//add drag capabilities  
var drag_handler = d3.drag()
	.on("start", drag_start)
	.on("drag", drag_drag)
	.on("end", drag_end);

drag_handler(node);


//add zoom capabilities 
var zoom_handler = d3.zoom()
    .on("zoom", zoom_actions);

zoom_handler(svg);

/** Functions **/

//Function to choose what color circle we have
//Let's return blue for males and red for females
function circleColour(d) {
    if (d.keyword) {
        return "red";
    } else {
        return "lightGreen";
    }
}

//Function to choose the line colour and thickness 
//If the link type is "A" return green 
//If the link type is "E" return red 
function linkColour(d) {
    return "black";
}

//Drag functions 
//d is the node 
function drag_start(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

//make sure you can't drag the circle outside the box
function drag_drag(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function drag_end(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

//Zoom functions 
function zoom_actions() {
    g.attr("transform", d3.event.transform)
}

function tickActions() {
    //update circle positions each tick of the simulation 
    node
     .attr("cx", function (d) { return d.x; })
     .attr("cy", function (d) { return d.y; });

    //update link positions 
    link
        .attr("x1", function (d) { return d.source.x; })
        .attr("y1", function (d) { return d.source.y; })
        .attr("x2", function (d) { return d.target.x; })
        .attr("y2", function (d) { return d.target.y; });
}