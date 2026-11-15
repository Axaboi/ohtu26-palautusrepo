*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    testaaja3
    Set Password    salasana1    salasana1
    Click    button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    xy
    Set Password    salasana1    salasana1
    Click    button >> text=Register
    Register Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    testaaja12
    Set Password    xy    xy
    Click    button >> text=Register
    Register Should Fail With Message    Password must be at least 3 characters long


Register With Username That Is Already In Use
    Set Username    testaaja
    Set Password    salasana2    salasana2
    Click    button >> text=Register
    Register Should Fail With Message    Username is already in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Get Text    body    *=    ${message}

Set Username
    [Arguments]    ${username}
    Fill Text    id=username    ${username}

Set Password
    [Arguments]    ${password}    ${password_conf}
    Fill Secret    id=password    $password
    Fill Secret    id=password_confirmation    $password_conf

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    testaaja    salasana1
    Go To Register Page