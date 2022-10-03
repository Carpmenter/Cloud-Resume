async function counter_fn() {
    var counter = document.getElementById("cntr");
    var url = 'https://l8q743vdmb.execute-api.us-east-1.amazonaws.com/prod'

    //GET current count of entries from DB
    const getResponse = await fetch(url);
    const getJson = await getResponse.json();
    console.log(getJson.body.length);
    var count = getJson.body.length;
    count++;
    counter.innerHTML = count;

    POST updated count to DB
    const postResponse = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({
            "countId": count
        })
    });
    const postJson = await postResponse.json();
    console.log(postJson);

  }
  window.onload = counter_fn;
