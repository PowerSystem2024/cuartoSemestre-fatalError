"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthenticationError = exports.AuthenticatorErrors = exports.PaymentRequestHandlerApplication = void 0;
var PaymentRequestHandlerApplication;
(function (PaymentRequestHandlerApplication) {
    PaymentRequestHandlerApplication["MercadoLibre"] = "ML";
    PaymentRequestHandlerApplication["MercadoPago"] = "MP";
})(PaymentRequestHandlerApplication = exports.PaymentRequestHandlerApplication || (exports.PaymentRequestHandlerApplication = {}));
var AuthenticatorErrors;
(function (AuthenticatorErrors) {
    AuthenticatorErrors["NotInitialized"] = "NOT_INITIALIZED";
    AuthenticatorErrors["AlreadyShowing"] = "ALREADY_SHOWING";
    AuthenticatorErrors["SiteIdNotSupported"] = "NOT_SUPPORTED_SITE_ID";
    AuthenticatorErrors["InvalidEmail"] = "INVALID_EMAIL_ADDRESS";
    AuthenticatorErrors["InvalidAmount"] = "INVALID_AMOUNT_VALUE";
    AuthenticatorErrors["PRApiError"] = "PAYMENT_REQUEST_ERROR";
    AuthenticatorErrors["PRApiNotSupported"] = "PAYMENT_REQUEST_NOT_SUPPORTED";
    AuthenticatorErrors["AuthenticationNotSupported"] = "AUTHENTICATION_FLOW_NOT_SUPPORTED";
    AuthenticatorErrors["NoApplicationsDetected"] = "NO_APPLICATIONS_DETECTED";
    AuthenticatorErrors["ApplicationCheckError"] = "APPLICATION_CHECK_ERROR";
    AuthenticatorErrors["ApiRequestFailed"] = "API_REQUEST_FAILED";
    AuthenticatorErrors["BottomsheetLoadingFailed"] = "BOTTOMSHEET_LOADING_FAILED";
    AuthenticatorErrors["BottomsheetCloseFailed"] = "BOTTOMSHEET_CLOSE_FAILED";
    AuthenticatorErrors["NoUserConfirmation"] = "NO_USER_CONFIRMATION";
    AuthenticatorErrors["UnreachableApplication"] = "UNREACHABLE_APPLICATION";
    AuthenticatorErrors["SecurityBlocked"] = "SECURITY_BLOCKED";
    AuthenticatorErrors["PublicKeyNotSet"] = "PUBLIC_KEY_NOT_SET";
    AuthenticatorErrors["InvalidPlatformId"] = "INVALID_PLATFORM_ID";
    AuthenticatorErrors["InvalidBricks"] = "INVALID_BRICKS";
})(AuthenticatorErrors = exports.AuthenticatorErrors || (exports.AuthenticatorErrors = {}));
class AuthenticationError extends Error {
    constructor(message, code) {
        super(message);
        this.name = 'AuthenticationError';
        this.code = code;
    }
}
exports.AuthenticationError = AuthenticationError;
