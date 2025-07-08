async function getData(id) {
  const url='http://localhost:8080/'+id
  try {
        const response = await fetch(url);
        console.log(response.status)
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        console.log(json);
        alert(JSON.stringify(json));
  
        } catch (error) {
            console.error(error.message);
            alert(error.message)
        }
}