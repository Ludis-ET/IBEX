{% extends 'base.html' %}
{% load static %}

{% block body %}
<div class="container mt-5 mb-5">
    <h2 class="text-center mb-4">Checkout</h2>
    <form id="checkout-form" method="post" action="{% url 'checkout' %}">
        {% csrf_token %}
        <div class="row">
            <div class="col-md-8">
                <div class="card p-4 mb-4">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_first_name">First Name</label>
                                {{ checkout_form.first_name }}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_last_name">Last Name</label>
                                {{ checkout_form.last_name }}
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="id_email">Email</label>
                        {{ checkout_form.email }}
                    </div>
                    <div class="form-group">
                        <label for="id_address">Address</label>
                        {{ checkout_form.address }}
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_city">City</label>
                                {{ checkout_form.city }}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_state">State</label>
                                {{ checkout_form.state }}
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_postal_code">Postal Code</label>
                                {{ checkout_form.postal_code }}
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="id_country">Country</label>
                                {{ checkout_form.country }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card p-4">
                    <h4 class="card-title">Cart Summary</h4>
                    <ul class="list-group list-group-flush mb-3">
                        {% for course in cart_courses %}
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            {{ course.title }}
                            <span>${{ course.price }}</span>
                        </li>
                        {% endfor %}
                    </ul>
                    <p class="text-right font-weight-bold">Total: ${{ total }}</p>
                    <div id="paypal-button-container">
                        <button type="submit" id="complete-order-button" class="btn btn-primary btn-block mt-3">Complete Order</button>
                    </div>
                </div>
            </div>
        </div>
    </form>
</div>

<script src="https://www.paypal.com/sdk/js?client-id={{ paypal_client_id }}"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        var form = document.getElementById('checkout-form');
        var completeOrderButton = document.getElementById('complete-order-button');

        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission before validation
            
            if (form.checkValidity()) {
                paypal.Buttons({
                    createOrder: function(data, actions) {
                        return actions.order.create({
                            purchase_units: [{
                                amount: {
                                    value: '{{ total }}'
                                }
                            }]
                        });
                    },
                    onApprove: function(data, actions) {
                        return actions.order.capture().then(function(details) {
                            var transactionInput = document.createElement('input');
                            transactionInput.type = 'hidden';
                            transactionInput.name = 'paypal_transaction_id';
                            transactionInput.value = details.id;
                            form.appendChild(transactionInput);

                            completeOrderButton.disabled = true; // Disable after successful submission

                            form.submit(); // Submit the form with PayPal transaction ID
                        });
                    }
                }).render('#paypal-button-container');
            } else {
                form.reportValidity();
            }
        });
    });
</script>
{% endblock %}
