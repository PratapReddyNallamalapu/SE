const resource_url = "https://vkkm38khe4.execute-api.us-east-1.amazonaws.com/dev/property";

async function fetchProperties() {
  try {
    const response = await fetch(resource_url);
    if (!response.ok) {
      throw new Error('Network response was not ok.');
    }
    const properties = await response.json();
    return properties;
  } catch (error) {
    console.error('Error fetching properties:', error);
    return [];
  }
}

function displayProperties() {
  const propertyList = document.getElementById("property-list");

  fetchProperties().then((properties) => {
    properties.forEach((property) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${property.str_address}</td>
        <td>${property.city}</td>
        <td>${property.state}</td>
        <td>${property.zip}</td>
        <td>${property.year}</td>
        <td>${property.type}</td>
        <td>${property.sqft}</td>
        <td>${property.beds}</td>
        <td>${property.baths}</td>
      `;
      propertyList.appendChild(row);
    });
  });
}

window.onload = displayProperties;
