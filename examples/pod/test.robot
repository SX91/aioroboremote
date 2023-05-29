*** Settings ***
Documentation     The test
Library  Remote  http://localhost:8270/pod  WITH NAME  POD
Library  Remote  http://localhost:8270/containers  WITH NAME  Containers

*** Test Cases ***
Run POD.Sum Floats method on remote
    ${result} =  POD.Sum Floats  1.5  3.5

Run POD.Sum Ints method on remote
    ${result} =  POD.Sum Ints  2  3

Run POD.Concat method on remote
    ${result} =  POD.Concat  fizz  buzz

Run Containers.Echo Dict method on remote
    ${result} =  Containers.Echo Dict  { "type": 123 }

Run Containers.Echo List method on remote
    ${result} =  Containers.Echo List  [ 123, 456, 789 ]

Run Containers.Echo Tuple method on remote
    ${result} =  Containers.Echo Tuple  ( 123, "456", 789.15 )
