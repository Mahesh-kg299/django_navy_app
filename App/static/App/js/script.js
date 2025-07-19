let getCSRFToken = () => {
    let cookies = document.cookie.split(";")
    let csrftoken = ""
    for (let cookie of cookies) {
        let [key, value] = cookie.split("=")
        if (key = 'csrftoken') {
            csrftoken = value
        }
    }
    return csrftoken
}

let getJsonData = async (url) => {
    let response = await fetch(url, {
            headers: {
                "Content-Type": "application/json"
            }
        })
    let jsonData = await response.json()
    return jsonData
}

let sendData = async (url, data) => {
    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify(data)
    })
    let returnText = await response.text()
    console.log(returnText)
}