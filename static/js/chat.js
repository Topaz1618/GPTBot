const socket = new WebSocket("ws://127.0.0.1:8888/ws");
const messagesDiv = document.getElementById("messages");
const inputField = document.getElementById("chat_input");
const sendButton = document.getElementById("sendButton");

socket.onopen = event => {
    console.log("WebSocket connection opened");
};

socket.onmessage = event => {
    const response = event.data;
    // console.log(response)
    displayResponse(response);
};


socket.onclose = event => {
    console.log("WebSocket connection closed");
};

var responseDiv;
var isCollecting = false;
var accumulatedResponse = "";

async function formatResponse(response) {
    if (response.includes("\n")){
        response = "<br>";
    }
    responseDiv.innerHTML += response;

}


function codeBtnCreator(){
    var button = document.createElement("button");
    button.className = "copy-button";
    button.setAttribute("onclick", "copyContent(this)");

    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.style.height = "16px";
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");

    var path1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path1.setAttribute("d", "M17 3H7C5.89543 3 5 3.89543 5 5V19C5 20.1046 5.89543 21 7 21H17C18.1046 21 19 20.1046 19 19V5C19 3.89543 18.1046 3 17 3Z");

    var path2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path2.setAttribute("d", "M15 1H9C7.89543 1 7 1.89543 7 3V5H17V3C17 1.89543 16.1046 1 15 1Z");

    var path3 = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path3.setAttribute("d", "M8 9H16");

    svg.appendChild(path1);
    svg.appendChild(path2);
    svg.appendChild(path3);

    button.appendChild(svg);

    var span = document.createElement("span");
    span.style.height = "16px";
    span.innerText = "Copy code";

    button.appendChild(span);

    return button

}


function displayResponse(response) {
    console.log(response)
    if (response === "START MSG") {
        isCollecting = true;
        is_code = false;
        end_flag = "";
        responseDiv = document.createElement("div");
        responseDiv.className = "bot"
        bot_content = document.createElement("div");
        bot_content.style.width = "50%";
        bot_content.style.marginLeft = "25%";

        bot_content.textContent = "";

        responseDiv.appendChild(bot_content)
        messagesDiv.appendChild(responseDiv);

    } else if (response === "END MSG") {
        isCollecting = false;
    } else {
        if (isCollecting) {
            // console.log(response);
            if (response.includes("\n")){
                response += "<br><br>";
            }

            console.log("code：", is_code);
            if (response.includes('```') && is_code == false){
                is_code = true;
                end_flag = "";
                CodeModel = document.createElement("div");
                CodeModel.className = "code-block";
                CodeModel.style.position = "relative"
                // CodeModel.style.width = "50%";
                // CodeModel.style.marginLeft = "25%";

                var CodeHeader = document.createElement("div");
                CodeHeader.className = "code-header"
                CodeHeader.style.height = "26px"

                var lang_info = document.createElement("span");
                lang_info.className = "language";
                lang_info.innerText = "python";

                var btn = codeBtnCreator();
                CodeHeader.appendChild(lang_info);
                CodeHeader.appendChild(btn);
                CodeModel.appendChild(CodeHeader);

                var CodePre = document.createElement("pre");

                Code = document.createElement("code");

                Code.className = "code language-python hljs";
                Code.style.marginTop = "28px";


                Code.innerHTML = ""

                CodePre.appendChild(Code);
                CodeModel.appendChild(CodePre);
                bot_content.appendChild(CodeModel)


            }else if(end_flag.includes('```') && is_code == true){
                is_code = false;
                end_flag = "";
                hljs.highlightBlock(Code);
                bot_content.innerHTML += response;

            }else if(is_code == true) {
                if(response.includes('`')){
                    end_flag += response;
                }else{
                    Code.innerHTML += response;
                }

            }else{
                bot_content.innerHTML += response;
            }

        }
    }
}

sendButton.addEventListener("click", () => {
    const userQuestion = inputField.value;
    if (userQuestion.trim() !== "") {
        displayMessage(`${userQuestion}`);
        socket.send(userQuestion);

        // Clear input field
        inputField.value = "";
    }
});

function displayMessage(message) {
    var user_model = document.createElement("div")
    user_model.className = "user";
    var user_content = document.createElement("div");
    user_content.style.width = "50%";
    user_content.style.marginLeft = "25%";

    user_content.innerHTML = message;
    user_model.appendChild(user_content);
    messagesDiv.appendChild(user_model);
}

inputField.addEventListener("keyup", event => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});


