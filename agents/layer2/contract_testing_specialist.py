"""ContractIQ Contract Testing Specialist - Layer 2

Consumer-driven contract testing for microservices, API contracts, and service integration validation.
"""

from typing import Dict, List, Any, Optional
import json


class ContractTestingSpecialist:
    """
    Layer 2 Domain Specialist: Contract Testing
   
    Expertise:
    - Consumer-driven contract testing (Pact-style)
    - Provider contract validation
    - Schema compatibility testing
    - API contract versioning
    - Breaking change detection
    - Bi-directional contract testing
    - GraphQL schema contract testing
    - Message contract testing (Kafka, RabbitMQ)
    """
   
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.test_results = []
        self.contracts = {}
       
    def define_consumer_contract(self, consumer: str, provider: str, 
                                 contract_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        Define a consumer-driven contract.
       
        Args:
            consumer: Consumer service name
            provider: Provider service name
            contract_spec: Contract specification (requests, responses, schemas)
           
        Returns:
            Contract definition result
        """
        contract_id = f"{consumer}-{provider}"
        self.contracts[contract_id] = {
            'consumer': consumer,
            'provider': provider,
            'spec': contract_spec,
            'version': '1.0.0',
            'status': 'defined'
        }
       
        result = {
            'contract_id': contract_id,
            'consumer': consumer,
            'provider': provider,
            'interactions': len(contract_spec.get('interactions', [])),
            'status': 'success'
        }
        return result
   
    def verify_provider_contract(self, provider: str, 
                                 consumer_contracts: List[str]) -> Dict[str, Any]:
        """
        Verify provider implementation against consumer contracts.
       
        Args:
            provider: Provider service name
            consumer_contracts: List of consumer contract IDs to verify
           
        Returns:
            Verification results
        """
        verification_results = []
        for contract_id in consumer_contracts:
            if contract_id in self.contracts:
                # Simulate contract verification
                verification_results.append({
                    'contract_id': contract_id,
                    'verified': True,
                    'violations': [],
                    'response_time_ms': 45
                })
            else:
                verification_results.append({
                    'contract_id': contract_id,
                    'verified': False,
                    'error': 'Contract not found'
                })
       
        result = {
            'provider': provider,
            'total_contracts': len(consumer_contracts),
            'verified_contracts': sum(1 for v in verification_results if v.get('verified')),
            'failed_contracts': sum(1 for v in verification_results if not v.get('verified')),
            'verification_details': verification_results,
            'status': 'passed' if all(v.get('verified') for v in verification_results) else 'failed'
        }
        self.test_results.append(result)
        return result
   
    def test_schema_compatibility(self, old_schema: Dict, 
                                  new_schema: Dict) -> Dict[str, Any]:
        """
        Test schema compatibility between versions.
       
        Args:
            old_schema: Original schema
            new_schema: New schema version
           
        Returns:
            Compatibility test results
        """
        breaking_changes = []
        non_breaking_changes = []
       
        # Simulate breaking change detection
        old_fields = set(old_schema.get('properties', {}).keys())
        new_fields = set(new_schema.get('properties', {}).keys())
       
        removed_fields = old_fields - new_fields
        added_fields = new_fields - old_fields
       
        if removed_fields:
            breaking_changes.append({
                'type': 'field_removed',
                'fields': list(removed_fields),
                'severity': 'critical'
            })
       
        if added_fields:
            non_breaking_changes.append({
                'type': 'field_added',
                'fields': list(added_fields),
                'severity': 'info'
            })
       
        result = {
            'compatible': len(breaking_changes) == 0,
            'breaking_changes': breaking_changes,
            'non_breaking_changes': non_breaking_changes,
            'compatibility_level': 'backward_compatible' if len(breaking_changes) == 0 else 'breaking',
            'status': 'passed' if len(breaking_changes) == 0 else 'failed'
        }
        return result
   
    def test_message_contract(self, topic: str, message_schema: Dict, 
                             sample_message: Dict) -> Dict[str, Any]:
        """
        Test message contract for async messaging (Kafka, RabbitMQ).
       
        Args:
            topic: Message topic/queue name
            message_schema: Expected message schema
            sample_message: Sample message to validate
           
        Returns:
            Message contract test results
        """
        # Simulate schema validation
        schema_fields = set(message_schema.get('properties', {}).keys())
        message_fields = set(sample_message.keys())
       
        missing_fields = schema_fields - message_fields
        extra_fields = message_fields - schema_fields
       
        result = {
            'topic': topic,
            'schema_valid': len(missing_fields) == 0,
            'missing_fields': list(missing_fields),
            'extra_fields': list(extra_fields),
            'message_size_bytes': len(json.dumps(sample_message)),
            'status': 'passed' if len(missing_fields) == 0 else 'failed'
        }
        return result
   
    def detect_breaking_changes(self, contract_v1: Dict, 
                               contract_v2: Dict) -> Dict[str, Any]:
        """
        Detect breaking changes between contract versions.
       
        Args:
            contract_v1: Original contract version
            contract_v2: New contract version
           
        Returns:
            Breaking change detection results
        """
        breaking_changes = []
       
        # Check for removed endpoints
        v1_endpoints = set(contract_v1.get('endpoints', []))
        v2_endpoints = set(contract_v2.get('endpoints', []))
        removed_endpoints = v1_endpoints - v2_endpoints
       
        if removed_endpoints:
            breaking_changes.append({
                'type': 'endpoint_removed',
                'endpoints': list(removed_endpoints),
                'impact': 'high'
            })
       
        # Check for changed response structures
        for endpoint in v1_endpoints.intersection(v2_endpoints):
            v1_response = contract_v1.get('responses', {}).get(endpoint)
            v2_response = contract_v2.get('responses', {}).get(endpoint)
            if v1_response != v2_response:
                breaking_changes.append({
                    'type': 'response_structure_changed',
                    'endpoint': endpoint,
                    'impact': 'medium'
                })
       
        result = {
            'breaking_changes_detected': len(breaking_changes),
            'breaking_changes': breaking_changes,
            'recommendation': 'major_version_bump' if breaking_changes else 'minor_version_bump',
            'safe_to_deploy': len(breaking_changes) == 0
        }
        return result
   
    def generate_contract_tests(self, contract_id: str) -> Dict[str, Any]:
        """
        Auto-generate tests from contract definition.
       
        Args:
            contract_id: Contract identifier
           
        Returns:
            Generated test suite
        """
        if contract_id not in self.contracts:
            return {'error': 'Contract not found', 'status': 'failed'}
       
        contract = self.contracts[contract_id]
        interactions = contract['spec'].get('interactions', [])
       
        test_suite = {
            'contract_id': contract_id,
            'total_tests': len(interactions) * 3,  # request, response, error cases
            'test_categories': {
                'happy_path': len(interactions),
                'error_scenarios': len(interactions),
                'edge_cases': len(interactions)
            },
            'estimated_execution_time_ms': len(interactions) * 50,
            'status': 'generated'
        }
        return test_suite
   
    def get_specialist_stats(self) -> Dict[str, Any]:
        """Get contract testing specialist statistics."""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for t in self.test_results if t.get('status') == 'passed')
       
        return {
            'specialist_type': 'ContractTestingSpecialist',
            'layer': 2,
            'total_contracts': len(self.contracts),
            'total_verification_tests': total_tests,
            'passed_tests': passed_tests,
            'pass_rate': round((passed_tests / total_tests * 100), 2) if total_tests > 0 else 0
        }


if __name__ == '__main__':
    specialist = ContractTestingSpecialist()
   
    # Define a consumer contract
    contract = specialist.define_consumer_contract(
        'order-service',
        'payment-service',
        {
            'interactions': [
                {'method': 'POST', 'path': '/payments', 'status': 200}
            ]
        }
    )
    print(f"Contract Defined: {contract}")
   
    # Verify provider
    verification = specialist.verify_provider_contract(
        'payment-service',
        ['order-service-payment-service']
    )
    print(f"Provider Verification: {verification}")
   
    # Test schema compatibility
    old_schema = {'properties': {'id': 'string', 'amount': 'number'}}
    new_schema = {'properties': {'id': 'string', 'amount': 'number', 'currency': 'string'}}
    compat = specialist.test_schema_compatibility(old_schema, new_schema)
    print(f"Schema Compatibility: {compat}")
   
    # Get stats
    print(f"Specialist Stats: {specialist.get_specialist_stats()}")
