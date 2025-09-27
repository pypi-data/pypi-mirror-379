*&---------------------------------------------------------------------*
*& Class SERIAL_SERVICE_METHOD
*&---------------------------------------------------------------------*
*& This class provides methods for calling the serialsrv software.
*& When serialsrv is called, it reads the serial port specified on the computer it's running on and returns a value.
*& This class parses the incoming value and provides it as a method result.
*& You can install serialsrv on a computer with Python installed:
*& using pip install serialsrv or pip3 install serialsrv.
*& For detailed information, please visit:
*& https://pypi.org/project/serialsrv
*& or
*& https://github.com/altaykirecci/serialsrv.
*& Author: Altay Kireççi (c)(p)2025-09
*&---------------------------------------------------------------------*

CLASS serial_service_method DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
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

    TYPES: BEGIN OF ty_serial_result,
             success     TYPE abap_bool,
             value       TYPE string,
             message     TYPE string,
             mode        TYPE string,
             result      TYPE string,
             timestamp   TYPE string,
             error_text  TYPE string,
           END OF ty_serial_result.

    CLASS-METHODS: call_serial_service
      IMPORTING
        iv_host        TYPE string DEFAULT 'localhost'
        iv_port        TYPE string DEFAULT '7373'
        iv_timeout     TYPE i DEFAULT 10
        iv_test_mode   TYPE abap_bool DEFAULT abap_false
      RETURNING
        VALUE(rs_result) TYPE ty_serial_result
      EXCEPTIONS
        connection_error
        timeout_error
        parse_error.

    CLASS-METHODS: get_serial_value
      IMPORTING
        iv_host        TYPE string DEFAULT 'localhost'
        iv_port        TYPE string DEFAULT '7373'
        iv_timeout     TYPE i DEFAULT 10
      RETURNING
        VALUE(rv_value) TYPE string
      EXCEPTIONS
        connection_error
        timeout_error
        parse_error.

    CLASS-METHODS: test_connection
      IMPORTING
        iv_host        TYPE string DEFAULT 'localhost'
        iv_port        TYPE string DEFAULT '7373'
        iv_timeout     TYPE i DEFAULT 5
      RETURNING
        VALUE(rv_success) TYPE abap_bool
      EXCEPTIONS
        connection_error
        timeout_error.

  PRIVATE SECTION.
    CLASS-METHODS: create_http_client
      IMPORTING
        iv_host        TYPE string
        iv_port        TYPE string
        iv_timeout     TYPE i
      RETURNING
        VALUE(ro_client) TYPE REF TO if_http_client
      EXCEPTIONS
        connection_error.

    CLASS-METHODS: parse_json_response
      IMPORTING
        iv_json        TYPE string
      RETURNING
        VALUE(rs_response) TYPE ty_response
      EXCEPTIONS
        parse_error.

    CLASS-METHODS: build_url
      IMPORTING
        iv_host        TYPE string
        iv_port        TYPE string
        iv_test_mode   TYPE abap_bool DEFAULT abap_false
      RETURNING
        VALUE(rv_url) TYPE string.

ENDCLASS.

CLASS serial_service_method IMPLEMENTATION.

  METHOD call_serial_service.
    DATA: lo_http_client TYPE REF TO if_http_client,
          lv_url         TYPE string,
          lv_response    TYPE string,
          lv_status_code TYPE i,
          lv_reason      TYPE string,
          ls_response    TYPE ty_response.

    " Initialize result
    CLEAR rs_result.

    " Build URL
    lv_url = build_url( iv_host = iv_host iv_port = iv_port iv_test_mode = iv_test_mode ).

    " Create HTTP client
    TRY.
        ro_client = create_http_client(
          iv_host = iv_host
          iv_port = iv_port
          iv_timeout = iv_timeout
        ).
      CATCH cx_root INTO DATA(lx_error).
        rs_result-success = abap_false.
        rs_result-error_text = lx_error->get_text( ).
        RAISE connection_error.
    ENDTRY.

    " Set request URI
    lo_http_client->request->set_method( if_http_request=>co_request_method_get ).
    lo_http_client->request->set_header_field( name = 'Content-Type' value = 'application/json' ).

    " Send request
    TRY.
        lo_http_client->send( ).
        lo_http_client->receive( ).
      CATCH cx_http_exception INTO DATA(lx_http_error).
        rs_result-success = abap_false.
        rs_result-error_text = lx_http_error->get_text( ).
        RAISE connection_error.
    ENDTRY.

    " Get response
    lo_http_client->response->get_status( IMPORTING code = lv_status_code reason = lv_reason ).
    lv_response = lo_http_client->response->get_cdata( ).

    " Check status code
    IF lv_status_code <> 200.
      rs_result-success = abap_false.
      rs_result-error_text = |HTTP Error { lv_status_code }: { lv_reason }|.
      RAISE connection_error.
    ENDIF.

    " Parse JSON response
    TRY.
        ls_response = parse_json_response( iv_json = lv_response ).
      CATCH cx_root INTO lx_error.
        rs_result-success = abap_false.
        rs_result-error_text = lx_error->get_text( ).
        RAISE parse_error.
    ENDTRY.

    " Fill result
    rs_result-success = abap_true.
    rs_result-value = ls_response-message-value.
    rs_result-message = ls_response-message-msg.
    rs_result-mode = ls_response-message-mode.
    rs_result-result = ls_response-message-result.
    rs_result-timestamp = ls_response-timestamp.

    " Close HTTP client
    lo_http_client->close( ).

  ENDMETHOD.

  METHOD get_serial_value.
    DATA: ls_result TYPE ty_serial_result.

    " Call serial service
    TRY.
        ls_result = call_serial_service(
          iv_host = iv_host
          iv_port = iv_port
          iv_timeout = iv_timeout
        ).
      CATCH cx_root.
        RAISE connection_error.
    ENDTRY.

    " Return value
    rv_value = ls_result-value.

  ENDMETHOD.

  METHOD test_connection.
    DATA: lo_http_client TYPE REF TO if_http_client,
          lv_url         TYPE string,
          lv_status_code TYPE i,
          lv_reason      TYPE string.

    " Initialize result
    rv_success = abap_false.

    " Build URL
    lv_url = build_url( iv_host = iv_host iv_port = iv_port iv_test_mode = abap_true ).

    " Create HTTP client
    TRY.
        ro_client = create_http_client(
          iv_host = iv_host
          iv_port = iv_port
          iv_timeout = iv_timeout
        ).
      CATCH cx_root.
        RAISE connection_error.
    ENDTRY.

    " Set request URI
    lo_http_client->request->set_method( if_http_request=>co_request_method_get ).

    " Send request
    TRY.
        lo_http_client->send( ).
        lo_http_client->receive( ).
      CATCH cx_http_exception.
        RAISE connection_error.
    ENDTRY.

    " Get response
    lo_http_client->response->get_status( IMPORTING code = lv_status_code reason = lv_reason ).

    " Check status code
    IF lv_status_code = 200.
      rv_success = abap_true.
    ENDIF.

    " Close HTTP client
    lo_http_client->close( ).

  ENDMETHOD.

  METHOD create_http_client.
    DATA: lv_url TYPE string.

    " Build URL
    lv_url = |http://{ iv_host }:{ iv_port }/|.

    " Create HTTP client
    TRY.
        cl_http_client=>create_by_url(
          EXPORTING
            url                = lv_url
            ssl_id             = 'ANONYM'
          IMPORTING
            client             = ro_client
        ).
      CATCH cx_http_exception INTO DATA(lx_error).
        RAISE connection_error.
    ENDTRY.

    " Set timeout
    ro_client->set_timeout( iv_timeout ).

  ENDMETHOD.

  METHOD parse_json_response.
    DATA: lo_json TYPE REF TO /ui2/cl_json.

    " Create JSON parser
    CREATE OBJECT lo_json.

    " Parse JSON
    TRY.
        lo_json->deserialize(
          EXPORTING
            json = iv_json
          CHANGING
            data = rs_response
        ).
      CATCH cx_root INTO DATA(lx_error).
        RAISE parse_error.
    ENDTRY.

  ENDMETHOD.

  METHOD build_url.
    IF iv_test_mode = abap_true.
      rv_url = |http://{ iv_host }:{ iv_port }/?test=1|.
    ELSE.
      rv_url = |http://{ iv_host }:{ iv_port }/|.
    ENDIF.
  ENDMETHOD.

ENDCLASS.

*&---------------------------------------------------------------------*
*& Example Usage:
*&---------------------------------------------------------------------*
*& DATA: ls_result TYPE serial_service_method=>ty_serial_result,
*&       lv_value  TYPE string.
*&
*& " Call serial service and get full result
*& TRY.
*&     ls_result = serial_service_method=>call_serial_service(
*&       iv_host = '192.168.1.100'
*&       iv_port = '7373'
*&       iv_timeout = 10
*&     ).
*&     IF ls_result-success = abap_true.
*&       WRITE: / 'Value:', ls_result-value,
*&                / 'Message:', ls_result-message,
*&                / 'Mode:', ls_result-mode,
*&                / 'Result:', ls_result-result.
*&     ELSE.
*&       WRITE: / 'Error:', ls_result-error_text.
*&     ENDIF.
*&   CATCH serial_service_method=>connection_error.
*&     WRITE: / 'Connection error occurred'.
*&   CATCH serial_service_method=>timeout_error.
*&     WRITE: / 'Timeout error occurred'.
*&   CATCH serial_service_method=>parse_error.
*&     WRITE: / 'Parse error occurred'.
*& ENDTRY.
*&
*& " Get only the value
*& TRY.
*&     lv_value = serial_service_method=>get_serial_value(
*&       iv_host = '192.168.1.100'
*&       iv_port = '7373'
*&     ).
*&     WRITE: / 'Serial Value:', lv_value.
*&   CATCH serial_service_method=>connection_error.
*&     WRITE: / 'Connection error occurred'.
*&   CATCH serial_service_method=>timeout_error.
*&     WRITE: / 'Timeout error occurred'.
*&   CATCH serial_service_method=>parse_error.
*&     WRITE: / 'Parse error occurred'.
*& ENDTRY.
*&
*& " Test connection
*& TRY.
*&     IF serial_service_method=>test_connection(
*&       iv_host = '192.168.1.100'
*&       iv_port = '7373'
*&     ) = abap_true.
*&       WRITE: / 'Connection successful'.
*&     ELSE.
*&       WRITE: / 'Connection failed'.
*&     ENDIF.
*&   CATCH serial_service_method=>connection_error.
*&     WRITE: / 'Connection error occurred'.
*&   CATCH serial_service_method=>timeout_error.
*&     WRITE: / 'Timeout error occurred'.
*& ENDTRY.
*&---------------------------------------------------------------------*
