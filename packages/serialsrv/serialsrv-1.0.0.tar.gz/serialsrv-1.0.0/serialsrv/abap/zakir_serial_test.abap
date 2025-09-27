*&---------------------------------------------------------------------*
*& Report ZAKIR_HTTP_CL
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
REPORT ZAKIR_HTTP_CL.
*&---------------------------------------------------------------------*
*& Report ZAKIR_HTTP_CL
*&---------------------------------------------------------------------*
*& Simple working ABAP program to call Python Hello World service
*&---------------------------------------------------------------------*

*  Data declarations
DATA: lo_http_client TYPE REF TO if_http_client,
      lv_url         TYPE string,
      lv_response    TYPE string,
      lv_status_code TYPE i,
      lv_reason      TYPE string,
      lv_json_data   TYPE string,
      lv_debug_info  TYPE string.

* JSON response structure
TYPES: BEGIN OF ty_message,
         value  TYPE string,
         msg    TYPE string,
         mode   TYPE string,
         result TYPE string,
       END OF ty_message.

TYPES: BEGIN OF ty_response,
         message   TYPE ty_message,
         timestamp TYPE string,
         method    TYPE string,
         path      TYPE string,
         client_ip TYPE string,
         client_port TYPE string,
       END OF ty_response.

DATA: ls_response TYPE ty_response,
      lv_message_value TYPE string,
      lv_message_msg   TYPE string,
      lv_message_mode  TYPE string,
      lv_message_result TYPE string.

* Selection screen
SELECTION-SCREEN BEGIN OF BLOCK b1 WITH FRAME TITLE TEXT-001.
PARAMETERS: p_host TYPE string DEFAULT 'localhost',
            p_port TYPE string DEFAULT '7373',
            p_post AS CHECKBOX DEFAULT abap_false.
SELECTION-SCREEN END OF BLOCK b1.

SELECTION-SCREEN BEGIN OF BLOCK b2 WITH FRAME TITLE TEXT-002.
PARAMETERS: p_local AS CHECKBOX DEFAULT abap_true,
            p_127   AS CHECKBOX DEFAULT abap_false,
            p_ip    AS CHECKBOX DEFAULT abap_false.
SELECTION-SCREEN END OF BLOCK b2.

SELECTION-SCREEN BEGIN OF BLOCK b3 WITH FRAME TITLE TEXT-003.
PARAMETERS: p_debug AS CHECKBOX DEFAULT abap_false,
            p_head  AS CHECKBOX DEFAULT abap_false.
SELECTION-SCREEN END OF BLOCK b3.

* Text elements
SELECTION-SCREEN COMMENT /1(50) TEXT-001.
SELECTION-SCREEN COMMENT /1(50) TEXT-002.

* Main processing
START-OF-SELECTION.

  " Network connectivity test first
  IF p_debug = abap_true.
    PERFORM test_network_connectivity.
    WRITE: / ''.
  ENDIF.

  " Test multiple connection options if requested
  IF p_local = abap_true OR p_127 = abap_true OR p_ip = abap_true.
    PERFORM test_multiple_connections.
  ELSE.
    " Single connection test
    PERFORM test_single_connection.
  ENDIF.

*&---------------------------------------------------------------------*
*& Form test_single_connection
*&---------------------------------------------------------------------*
*& Test single connection with specified parameters
*&---------------------------------------------------------------------*
FORM test_single_connection.

  " Build URL
  CONCATENATE 'http://' p_host ':' p_port '/' INTO lv_url.

  WRITE: / 'Calling Python Hello World Service',
         / 'URL:', lv_url,
         / 'Method:', COND string( WHEN p_post = abap_true THEN 'POST' ELSE 'GET' ),
         / 'Host:', p_host,
         / 'Port:', p_port,
         / 'Current User:', sy-uname,
         / 'Current Date/Time:', sy-datum, sy-uzeit.

  " Debug mode information
  IF p_debug = abap_true.
    WRITE: / '----------------------------------------',
           / 'DEBUG MODE INFORMATION:',
           / 'System ID:', sy-sysid,
           / 'Client:', sy-mandt,
           / 'Application Server:', sy-host,
           / 'SAP Release:', sy-saprl,
           / 'Database:', sy-dbsys,
           / '----------------------------------------'.
  ENDIF.

  " Create HTTP client
  cl_http_client=>create_by_url(
    EXPORTING
      url                = lv_url
    IMPORTING
      client             = lo_http_client
    EXCEPTIONS
      argument_not_found = 1
      plugin_not_active  = 2
      internal_error     = 3
      OTHERS             = 4
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: Argument not found - Invalid URL format:', lv_url.
      WHEN 2.
        WRITE: / 'ERROR: HTTP plugin not active - Check HTTP client configuration'.
      WHEN 3.
        WRITE: / 'ERROR: Internal error in HTTP client creation'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error creating HTTP client. Return code:', sy-subrc.
    ENDCASE.
    EXIT.
  ENDIF.

  " Set HTTP client properties
  lo_http_client->propertytype_logon_popup = if_http_client=>co_disabled.
  lo_http_client->propertytype_accept_cookie = if_http_client=>co_enabled.

  " Set request headers
  lo_http_client->request->set_header_field(
    name  = 'Content-Type'
    value = 'application/json'
  ).

  lo_http_client->request->set_header_field(
    name  = 'Accept'
    value = 'application/json'
  ).

  lo_http_client->request->set_header_field(
    name  = 'User-Agent'
    value = 'ABAP-HTTP-Client/1.0'
  ).

  " Set request method and data
  IF p_post = abap_true.
    " POST request with JSON data
    lv_json_data = '{"test": "data", "message": "Hello from ABAP", "timestamp": "' && sy-datum && 'T' && sy-uzeit && '"}'.

    lo_http_client->request->set_method( if_http_request=>co_request_method_post ).
    lo_http_client->request->set_cdata( lv_json_data ).

    WRITE: / 'POST Data:', lv_json_data.
  ELSE.
    " GET request
    lo_http_client->request->set_method( if_http_request=>co_request_method_get ).
  ENDIF.

  " Send request
  lo_http_client->send(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      http_invalid_timeout       = 4
      OTHERS                     = 5
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: HTTP communication failure - Check network connection and server status'.
        WRITE: / '       Make sure Python service is running on:', lv_url.
        WRITE: / '       Troubleshooting steps:'.
        WRITE: / '       1. Check if Python service is running: python3 hello_service.py'.
        WRITE: / '       2. Test with curl: curl http://localhost:7373'.
        WRITE: / '       3. Check firewall settings'.
        WRITE: / '       4. Verify network connectivity'.
        WRITE: / '       5. Check ABAP HTTP client configuration'.
      WHEN 2.
        WRITE: / 'ERROR: HTTP client in invalid state - Client may be already closed'.
      WHEN 3.
        WRITE: / 'ERROR: HTTP processing failed - Check request format and headers'.
      WHEN 4.
        WRITE: / 'ERROR: HTTP invalid timeout - Timeout value is invalid'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error sending request. Return code:', sy-subrc.
    ENDCASE.
    lo_http_client->close( ).
    EXIT.
  ENDIF.

  " Receive response
  lo_http_client->receive(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      OTHERS                     = 4
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: HTTP communication failure while receiving response'.
        WRITE: / '       Server may be unreachable or connection lost'.
      WHEN 2.
        WRITE: / 'ERROR: HTTP client in invalid state while receiving response'.
      WHEN 3.
        WRITE: / 'ERROR: HTTP processing failed while receiving response'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error receiving response. Return code:', sy-subrc.
    ENDCASE.
    lo_http_client->close( ).
    EXIT.
  ENDIF.

  " Get response data
  lo_http_client->response->get_status(
    IMPORTING
      code   = lv_status_code
      reason = lv_reason
  ).

  lv_response = lo_http_client->response->get_cdata( ).

  " Display results
  WRITE: / '----------------------------------------',
         / 'Response Status Code:', lv_status_code,
         / 'Response Reason:', lv_reason.

  " Show response headers in debug mode
  IF p_head = abap_true.
    WRITE: / '----------------------------------------',
           / 'RESPONSE HEADERS:'.
    DATA: lo_response TYPE REF TO if_http_response.
    lo_response = lo_http_client->response.
    DATA: lv_header_name TYPE string,
          lv_header_value TYPE string.

    " Get all response headers
    DATA: lt_headers TYPE tihttpnvp.
    lo_response->get_header_fields( CHANGING fields = lt_headers ).

    LOOP AT lt_headers INTO DATA(ls_header).
      WRITE: / ls_header-name, ':', ls_header-value.
    ENDLOOP.
    WRITE: / '----------------------------------------'.
  ENDIF.

  " Check HTTP status code and display appropriate message
  IF lv_status_code >= 200 AND lv_status_code < 300.
    WRITE: / 'SUCCESS: Request completed successfully'.
  ELSEIF lv_status_code >= 300 AND lv_status_code < 400.
    WRITE: / 'WARNING: Redirection response - Status code:', lv_status_code.
  ELSEIF lv_status_code >= 400 AND lv_status_code < 500.
    CASE lv_status_code.
      WHEN 400.
        WRITE: / 'ERROR: Bad Request - Invalid request format or parameters'.
      WHEN 401.
        WRITE: / 'ERROR: Unauthorized - Authentication required'.
      WHEN 403.
        WRITE: / 'ERROR: Forbidden - Access denied'.
      WHEN 404.
        WRITE: / 'ERROR: Not Found - URL or resource not found'.
      WHEN 405.
        WRITE: / 'ERROR: Method Not Allowed - HTTP method not supported'.
      WHEN 408.
        WRITE: / 'ERROR: Request Timeout - Server timeout'.
      WHEN 429.
        WRITE: / 'ERROR: Too Many Requests - Rate limit exceeded'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Client Error - Status code:', lv_status_code.
    ENDCASE.
  ELSEIF lv_status_code >= 500.
    CASE lv_status_code.
      WHEN 500.
        WRITE: / 'ERROR: Internal Server Error - Server encountered an error'.
      WHEN 501.
        WRITE: / 'ERROR: Not Implemented - Server does not support the request'.
      WHEN 502.
        WRITE: / 'ERROR: Bad Gateway - Invalid response from upstream server'.
      WHEN 503.
        WRITE: / 'ERROR: Service Unavailable - Server temporarily unavailable'.
      WHEN 504.
        WRITE: / 'ERROR: Gateway Timeout - Upstream server timeout'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Server Error - Status code:', lv_status_code.
    ENDCASE.
  ELSE.
    WRITE: / 'WARNING: Unknown status code:', lv_status_code.
  ENDIF.

  WRITE: / '----------------------------------------',
         / 'Response Body:',
         / lv_response.

  " Parse JSON response if successful
  IF lv_status_code >= 200 AND lv_status_code < 300.
    PERFORM parse_json_response USING lv_response.
  ENDIF.

  " Close HTTP client
  lo_http_client->close( ).

ENDFORM.

*&---------------------------------------------------------------------*
*& Form parse_json_response
*&---------------------------------------------------------------------*
*& Parse JSON response using /ui2/cl_json=>deserialize
*&---------------------------------------------------------------------*
FORM parse_json_response USING pv_response TYPE string.

  DATA: lv_json TYPE string.

  " Initialize variables
  CLEAR: ls_response, lv_message_value, lv_message_msg, lv_message_mode, lv_message_result.

  " Use SAP's JSON deserializer
  lv_json = pv_response.
  
  TRY.
    CALL METHOD /ui2/cl_json=>deserialize
      EXPORTING
        json = lv_json
      CHANGING
        data = ls_response.
    
    " Extract message values
    lv_message_value = ls_response-message-value.
    lv_message_msg = ls_response-message-msg.
    lv_message_mode = ls_response-message-mode.
    lv_message_result = ls_response-message-result.
    
    " Display parsed values
    WRITE: / '----------------------------------------',
           / 'PARSED MESSAGE VALUES (using /ui2/cl_json):',
           / 'Value:', lv_message_value,
           / 'Message:', lv_message_msg,
           / 'Mode:', lv_message_mode,
           / 'Result:', lv_message_result,
           / 'Timestamp:', ls_response-timestamp,
           / 'Method:', ls_response-method,
           / 'Client IP:', ls_response-client_ip,
           / '----------------------------------------'.
           
  CATCH cx_sy_move_cast_error.
    WRITE: / 'ERROR: JSON deserialization failed - Invalid JSON format'.
    WRITE: / 'Raw response:', pv_response.
  CATCH cx_root INTO DATA(lx_error).
    WRITE: / 'ERROR: JSON deserialization failed:', lx_error->get_text( ).
    WRITE: / 'Raw response:', pv_response.
  ENDTRY.

ENDFORM.

*&---------------------------------------------------------------------*
*& Form test_multiple_connections
*&---------------------------------------------------------------------*
*& Test multiple connection options
*&---------------------------------------------------------------------*
FORM test_multiple_connections.

  DATA: lv_test_host TYPE string.

  WRITE: / '========================================',
         / 'Testing Multiple Connection Options',
         / '========================================'.

  " Test localhost
  IF p_local = abap_true.
    lv_test_host = 'localhost'.
    WRITE: / '----------------------------------------',
           / 'Testing localhost connection'.
    PERFORM test_connection_with_host USING lv_test_host.
  ENDIF.

  " Test 127.0.0.1
  IF p_127 = abap_true.
    lv_test_host = '127.0.0.1'.
    WRITE: / '----------------------------------------',
           / 'Testing 127.0.0.1 connection'.
    PERFORM test_connection_with_host USING lv_test_host.
  ENDIF.

  " Test custom IP (if provided)
  IF p_ip = abap_true AND p_host <> 'localhost' AND p_host <> '127.0.0.1'.
    lv_test_host = p_host.
    WRITE: / '----------------------------------------',
           / 'Testing custom host connection'.
    PERFORM test_connection_with_host USING lv_test_host.
  ENDIF.

  WRITE: / '========================================',
         / 'Multiple Connection Test Completed'.

ENDFORM.

*&---------------------------------------------------------------------*
*& Form test_connection_with_host
*&---------------------------------------------------------------------*
*& Test connection with specific host
*&---------------------------------------------------------------------*
FORM test_connection_with_host USING pv_host TYPE string.

  DATA: lv_url         TYPE string,
        lo_http_client TYPE REF TO if_http_client,
        lv_response    TYPE string,
        lv_status_code TYPE i,
        lv_reason      TYPE string.

  " Build URL
  CONCATENATE 'http://' pv_host ':' p_port '/' INTO lv_url.

  WRITE: / 'URL:', lv_url.

  " Create HTTP client
  cl_http_client=>create_by_url(
    EXPORTING
      url                = lv_url
    IMPORTING
      client             = lo_http_client
    EXCEPTIONS
      argument_not_found = 1
      plugin_not_active  = 2
      internal_error     = 3
      OTHERS             = 4
  ).

  IF sy-subrc <> 0.
    WRITE: / 'ERROR: Failed to create HTTP client for', pv_host, '- Return code:', sy-subrc.
    RETURN.
  ENDIF.

    " Set HTTP client properties
    lo_http_client->propertytype_logon_popup = if_http_client=>co_disabled.
    lo_http_client->propertytype_accept_cookie = if_http_client=>co_enabled.

  " Set headers
  lo_http_client->request->set_header_field(
    name  = 'Content-Type'
    value = 'application/json'
  ).

  lo_http_client->request->set_header_field(
    name  = 'Accept'
    value = 'application/json'
  ).

  lo_http_client->request->set_header_field(
    name  = 'User-Agent'
    value = 'ABAP-HTTP-Client/1.0'
  ).

  " Set GET method
  lo_http_client->request->set_method( if_http_request=>co_request_method_get ).

  " Send request
  lo_http_client->send(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      http_invalid_timeout       = 4
      OTHERS                     = 5
  ).

  IF sy-subrc <> 0.
    WRITE: / 'ERROR: Failed to send request to', pv_host, '- Return code:', sy-subrc.
    lo_http_client->close( ).
    RETURN.
  ENDIF.

  " Receive response
  lo_http_client->receive(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      OTHERS                     = 4
  ).

  IF sy-subrc <> 0.
    WRITE: / 'ERROR: Failed to receive response from', pv_host, '- Return code:', sy-subrc.
    lo_http_client->close( ).
    RETURN.
  ENDIF.

  " Get response
  lo_http_client->response->get_status(
    IMPORTING
      code   = lv_status_code
      reason = lv_reason
  ).

  lv_response = lo_http_client->response->get_cdata( ).

  " Display results
  IF lv_status_code = 200.
    WRITE: / 'SUCCESS: Connection to', pv_host, 'successful'.
    WRITE: / 'Response:', lv_response.
    " Parse JSON response
    PERFORM parse_json_response USING lv_response.
  ELSE.
    WRITE: / 'WARNING: Connection to', pv_host, 'returned status:', lv_status_code.
    WRITE: / 'Response:', lv_response.
  ENDIF.

  " Close client
  lo_http_client->close( ).

ENDFORM.

*&---------------------------------------------------------------------*
*& Form test_network_connectivity
*&---------------------------------------------------------------------*
*& Test basic network connectivity
*&---------------------------------------------------------------------*
FORM test_network_connectivity.

  WRITE: / '========================================',
         / 'Network Connectivity Test',
         / '========================================'.

  " Test different hosts
  DATA: lt_hosts TYPE TABLE OF string.
  APPEND 'localhost' TO lt_hosts.
  APPEND '127.0.0.1' TO lt_hosts.
  APPEND '8.8.8.8' TO lt_hosts.  " Google DNS
  APPEND '1.1.1.1' TO lt_hosts.  " Cloudflare DNS

  LOOP AT lt_hosts INTO DATA(lv_test_host).
    WRITE: / '----------------------------------------',
           / 'Testing connectivity to:', lv_test_host.

    " Try to create HTTP client with short timeout
    DATA: lo_test_client TYPE REF TO if_http_client.

    CONCATENATE 'http://' lv_test_host ':80' INTO DATA(lv_test_url).

    cl_http_client=>create_by_url(
      EXPORTING
        url                = lv_test_url
      IMPORTING
        client             = lo_test_client
      EXCEPTIONS
        argument_not_found = 1
        plugin_not_active  = 2
        internal_error     = 3
        OTHERS             = 4
    ).

    IF sy-subrc = 0.
    " Set HTTP client properties
    lo_test_client->propertytype_logon_popup = if_http_client=>co_disabled.

      " Try to send request
      lo_test_client->send(
        EXCEPTIONS
          http_communication_failure = 1
          http_invalid_state         = 2
          http_processing_failed     = 3
          http_invalid_timeout       = 4
          OTHERS                     = 5
      ).

      IF sy-subrc = 0.
        WRITE: / 'SUCCESS: Network connectivity to', lv_test_host, 'is working'.
      ELSE.
        WRITE: / 'WARNING: Network connectivity to', lv_test_host, 'failed - Return code:', sy-subrc.
      ENDIF.

      lo_test_client->close( ).
    ELSE.
      WRITE: / 'ERROR: Cannot create HTTP client for', lv_test_host, '- Return code:', sy-subrc.
    ENDIF.
  ENDLOOP.

  WRITE: / '========================================',
         / 'Network Connectivity Test Completed'.

ENDFORM.

*&---------------------------------------------------------------------*
*& Form test_post_request
*&---------------------------------------------------------------------*
*& Test POST request with JSON data
*&---------------------------------------------------------------------*
FORM test_post_request.

  DATA: lv_url         TYPE string,
        lo_http_client TYPE REF TO if_http_client,
        lv_response    TYPE string,
        lv_status_code TYPE i,
        lv_reason      TYPE string,
        lv_json_data   TYPE string.

  " Build URL
  CONCATENATE 'http://' p_host ':' p_port '/' INTO lv_url.

  WRITE: / '========================================',
         / 'Testing POST Request',
         / '========================================',
         / 'URL:', lv_url.

  " Create HTTP client
  cl_http_client=>create_by_url(
    EXPORTING
      url                = lv_url
    IMPORTING
      client             = lo_http_client
    EXCEPTIONS
      argument_not_found = 1
      plugin_not_active  = 2
      internal_error     = 3
      OTHERS             = 4
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: Argument not found - Invalid URL format:', lv_url.
      WHEN 2.
        WRITE: / 'ERROR: HTTP plugin not active - Check HTTP client configuration'.
      WHEN 3.
        WRITE: / 'ERROR: Internal error in HTTP client creation'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error creating HTTP client. Return code:', sy-subrc.
    ENDCASE.
    RETURN.
  ENDIF.

  " Set headers
  lo_http_client->request->set_header_field(
    name  = 'Content-Type'
    value = 'application/json'
  ).

  lo_http_client->request->set_header_field(
    name  = 'Accept'
    value = 'application/json'
  ).

  " Prepare JSON data
  lv_json_data = '{"test": "data", "message": "Hello from ABAP POST", "timestamp": "' && sy-datum && 'T' && sy-uzeit && '", "user": "' && sy-uname && '"}'.

  WRITE: / 'POST Data:', lv_json_data.

  " Set POST method and data
  lo_http_client->request->set_method( if_http_request=>co_request_method_post ).
  lo_http_client->request->set_cdata( lv_json_data ).

  " Send request
  lo_http_client->send(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      http_invalid_timeout       = 4
      OTHERS                     = 5
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: HTTP communication failure - Check network connection and server status'.
        WRITE: / '       Make sure Python service is running on:', lv_url.
      WHEN 2.
        WRITE: / 'ERROR: HTTP client in invalid state - Client may be already closed'.
      WHEN 3.
        WRITE: / 'ERROR: HTTP processing failed - Check request format and headers'.
      WHEN 4.
        WRITE: / 'ERROR: HTTP invalid timeout - Timeout value is invalid'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error sending request. Return code:', sy-subrc.
    ENDCASE.
    lo_http_client->close( ).
    RETURN.
  ENDIF.

  " Receive response
  lo_http_client->receive(
    EXCEPTIONS
      http_communication_failure = 1
      http_invalid_state         = 2
      http_processing_failed     = 3
      OTHERS                     = 4
  ).

  IF sy-subrc <> 0.
    CASE sy-subrc.
      WHEN 1.
        WRITE: / 'ERROR: HTTP communication failure while receiving response'.
        WRITE: / '       Server may be unreachable or connection lost'.
      WHEN 2.
        WRITE: / 'ERROR: HTTP client in invalid state while receiving response'.
      WHEN 3.
        WRITE: / 'ERROR: HTTP processing failed while receiving response'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Unknown error receiving response. Return code:', sy-subrc.
    ENDCASE.
    lo_http_client->close( ).
    RETURN.
  ENDIF.

  " Get response
  lo_http_client->response->get_status(
    IMPORTING
      code   = lv_status_code
      reason = lv_reason
  ).

  lv_response = lo_http_client->response->get_cdata( ).

  " Display results
  WRITE: / 'Status:', lv_status_code, lv_reason.

  " Check HTTP status code and display appropriate message
  IF lv_status_code >= 200 AND lv_status_code < 300.
    WRITE: / 'SUCCESS: POST request completed successfully'.
  ELSEIF lv_status_code >= 300 AND lv_status_code < 400.
    WRITE: / 'WARNING: Redirection response - Status code:', lv_status_code.
  ELSEIF lv_status_code >= 400 AND lv_status_code < 500.
    CASE lv_status_code.
      WHEN 400.
        WRITE: / 'ERROR: Bad Request - Invalid POST data format'.
      WHEN 401.
        WRITE: / 'ERROR: Unauthorized - Authentication required'.
      WHEN 403.
        WRITE: / 'ERROR: Forbidden - Access denied'.
      WHEN 404.
        WRITE: / 'ERROR: Not Found - URL or resource not found'.
      WHEN 405.
        WRITE: / 'ERROR: Method Not Allowed - POST method not supported'.
      WHEN 408.
        WRITE: / 'ERROR: Request Timeout - Server timeout'.
      WHEN 429.
        WRITE: / 'ERROR: Too Many Requests - Rate limit exceeded'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Client Error - Status code:', lv_status_code.
    ENDCASE.
  ELSEIF lv_status_code >= 500.
    CASE lv_status_code.
      WHEN 500.
        WRITE: / 'ERROR: Internal Server Error - Server encountered an error'.
      WHEN 501.
        WRITE: / 'ERROR: Not Implemented - Server does not support POST requests'.
      WHEN 502.
        WRITE: / 'ERROR: Bad Gateway - Invalid response from upstream server'.
      WHEN 503.
        WRITE: / 'ERROR: Service Unavailable - Server temporarily unavailable'.
      WHEN 504.
        WRITE: / 'ERROR: Gateway Timeout - Upstream server timeout'.
      WHEN OTHERS.
        WRITE: / 'ERROR: Server Error - Status code:', lv_status_code.
    ENDCASE.
  ELSE.
    WRITE: / 'WARNING: Unknown status code:', lv_status_code.
  ENDIF.

  WRITE: / 'Response:', lv_response.

  " Parse JSON response if successful
  IF lv_status_code >= 200 AND lv_status_code < 300.
    PERFORM parse_json_response USING lv_response.
  ENDIF.

  " Close client
  lo_http_client->close( ).

  WRITE: / '========================================',
         / 'POST Request Test Completed'.

ENDFORM.
