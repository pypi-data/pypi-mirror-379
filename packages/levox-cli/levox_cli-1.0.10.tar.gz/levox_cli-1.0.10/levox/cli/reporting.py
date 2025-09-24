"""
Levox Report Generator

This module handles report generation in various formats (JSON, HTML, PDF, SARIF).
Reports are only generated when explicitly requested, preventing unintended file creation.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
import uuid

from ..core.config import Config
from ..models.detection_result import DetectionResult
from .output import OutputManager

class ReportGenerator:
    """Generates professional reports in various formats."""
    
    def __init__(self, config: Config, output_manager: OutputManager):
        """Initialize the report generator."""
        self.config = config
        self.output_manager = output_manager
        self.report_dir = self._get_report_directory()
    
    def generate_report(self, results: DetectionResult, format_type: str, 
                       scan_time: float, license_tier: str) -> Optional[str]:
        """Generate a report in the specified format."""
        try:
            if format_type == 'json':
                return self._generate_json_report(results, scan_time, license_tier)
            elif format_type == 'html':
                return self._generate_html_report(results, scan_time, license_tier)
            elif format_type == 'pdf':
                return self._generate_pdf_report(results, scan_time, license_tier)
            elif format_type == 'sarif':
                return self._generate_sarif_report(results, scan_time, license_tier)
            else:
                self.output_manager.print_warning(f"Unsupported report format: {format_type}")
                return None
                
        except Exception as e:
            self.output_manager.print_error(f"Failed to generate {format_type} report: {e}")
            return None
    
    def generate_report_from_file(self, results: Union[DetectionResult, Dict[str, Any]], format_type: str,
                                 output_file: Optional[str], template: Optional[str],
                                 include_metadata: bool) -> Optional[str]:
        """Generate a report from file results."""
        try:
            # Handle new scan results format
            if isinstance(results, dict):
                # New format: {'scan_metadata': {...}, 'scan_results': {...}}
                scan_results = results.get('scan_results', {})
                scan_metadata = results.get('scan_metadata', {})
                
                # Convert scan_results back to DetectionResult-like structure for compatibility
                if 'file_results' in scan_results:
                    # Already in the right format
                    processed_results = scan_results
                else:
                    # Need to restructure the data
                    processed_results = self._restructure_scan_results(scan_results)
            else:
                # Old format: direct DetectionResult
                processed_results = results
                scan_metadata = {}
            
            if format_type == 'json':
                return self._generate_json_report_from_file(processed_results, output_file, include_metadata)
            elif format_type == 'html':
                return self._generate_html_report_from_file(processed_results, output_file, template, include_metadata)
            elif format_type == 'pdf':
                return self._generate_pdf_report_from_file(processed_results, output_file, template, include_metadata)
            elif format_type == 'sarif':
                return self._generate_sarif_report_from_file(processed_results, output_file, include_metadata)
            else:
                self.output_manager.print_warning(f"Unsupported report format: {format_type}")
                return None
                
        except Exception as e:
            self.output_manager.print_error(f"Failed to generate {format_type} report: {e}")
            return None
    
    def _get_report_directory(self) -> Path:
        """Get the directory for storing reports."""
        # Try to use configured report directory
        if hasattr(self.config, 'report_directory') and self.config.report_directory:
            report_dir = Path(self.config.report_directory)
        else:
            # Default to user's home directory
            report_dir = Path.home() / ".levox" / "reports"
        
        # Create directory if it doesn't exist
        report_dir.mkdir(parents=True, exist_ok=True)
        return report_dir
    
    def _generate_json_report(self, results: DetectionResult, scan_time: float, 
                             license_tier: str) -> str:
        """Generate a JSON report."""
        report_data = self._prepare_report_data(results, scan_time, license_tier)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"levox_report_{timestamp}.json"
        report_path = self.report_dir / filename
        
        # Write report
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        return str(report_path)
    
    def _generate_html_report(self, results: DetectionResult, scan_time: float, 
                             license_tier: str) -> str:
        """Generate an HTML report."""
        html_content = self._generate_html_content(results, scan_time, license_tier)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"levox_report_{timestamp}.html"
        report_path = self.report_dir / filename
        
        # Write report
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(report_path)
    
    def _generate_pdf_report(self, results: DetectionResult, scan_time: float, 
                            license_tier: str) -> str:
        """Generate a PDF report."""
        try:
            # Try to import weasyprint for PDF generation
            try:
                from weasyprint import HTML
            except ImportError:
                # Fallback to html2pdf if weasyprint not available
                try:
                    import pdfkit
                    use_pdfkit = True
                except ImportError:
                    self.output_manager.print_warning("PDF generation requires weasyprint or pdfkit. Installing weasyprint is recommended.")
                    return None
            
            # Generate HTML content first
            html_content = self._generate_html_content(results, scan_time, license_tier)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"levox_report_{timestamp}.pdf"
            report_path = self.report_dir / filename
            
            # Convert HTML to PDF
            if 'use_pdfkit' in locals() and use_pdfkit:
                # Use pdfkit (requires wkhtmltopdf)
                pdfkit.from_string(html_content, str(report_path))
            else:
                # Use weasyprint
                HTML(string=html_content).write_pdf(str(report_path))
            
            return str(report_path)
            
        except Exception as e:
            self.output_manager.print_warning(f"PDF generation failed: {e}")
            return None
    
    def _generate_sarif_report(self, results: DetectionResult, scan_time: float, 
                              license_tier: str) -> str:
        """Generate a SARIF report."""
        sarif_data = self._prepare_sarif_data(results, scan_time, license_tier)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"levox_report_{timestamp}.sarif"
        report_path = self.report_dir / filename
        
        # Write report
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(sarif_data, f, indent=2, ensure_ascii=False)
        
        return str(report_path)
    
    def _generate_json_report_from_file(self, results: Union[DetectionResult, Dict[str, Any]], 
                                       output_file: Optional[str], 
                                       include_metadata: bool) -> Optional[str]:
        """Generate JSON report from file results."""
        # Handle both DetectionResult objects and dictionaries
        if isinstance(results, dict):
            # Check if this is already restructured data
            if 'file_results' in results and 'total_issues_found' in results:
                # Data is already in the right format
                report_data = results.copy()
            else:
                # Extract scan results from the new format
                scan_results = results.get('scan_results', {})
                scan_metadata = results.get('scan_metadata', {})
                
                # Convert to JSON format
                if 'results' in scan_results:
                    report_data = {
                        'total_issues_found': scan_results.get('scan_summary', {}).get('total_matches', 0),
                        'total_files_scanned': scan_results.get('scan_summary', {}).get('total_files', 0),
                        'scan_path': scan_results.get('scan_summary', {}).get('scan_path', 'Unknown'),
                        'file_results': scan_results['results']
                    }
                else:
                    report_data = scan_results
        else:
            # Handle DetectionResult object
            report_data = self.output_manager._convert_to_json(results)
            scan_metadata = {}
        
        if include_metadata:
            report_data['metadata'] = {
                'generated_at': datetime.now().isoformat(),
                'levox_version': '0.9.0',
                'report_type': 'json',
                'scan_metadata': scan_metadata
            }
        
        # Always save to file for clean terminal output
        if not output_file:
            # Generate a default filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            scan_name = "scan_report"
            if hasattr(results, 'scan_path') and results.scan_path:
                scan_name = Path(results['scan_path']).name
            elif isinstance(results, dict) and 'scan_path' in results:
                scan_name = Path(results['scan_path']).name
            
            output_file = f"levox_report_{scan_name}_{timestamp}.json"
        
        # Write to output file
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        return str(output_path)
    
    def _generate_html_report_from_file(self, results: DetectionResult, 
                                       output_file: Optional[str], 
                                       template: Optional[str],
                                       include_metadata: bool) -> Optional[str]:
        """Generate HTML report from file results."""
        html_content = self._generate_html_content(results, 0.0, 'enterprise', include_metadata)
        
        # Always save to file for clean terminal output
        if not output_file:
            # Generate a default filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            scan_name = "scan_report"
            if hasattr(results, 'scan_path') and results.scan_path:
                scan_name = Path(results.scan_path).name
            elif isinstance(results, dict) and 'scan_path' in results:
                scan_name = Path(results['scan_path']).name
            
            output_file = f"levox_report_{scan_name}_{timestamp}.html"
        
        # Write to output file
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(output_path)
    
    def _generate_pdf_report_from_file(self, results: DetectionResult, 
                                      output_file: Optional[str], 
                                      template: Optional[str],
                                      include_metadata: bool) -> Optional[str]:
        """Generate PDF report from file results."""
        return self._generate_pdf_report(results, 0.0, 'enterprise')
    
    def _generate_sarif_report_from_file(self, results: DetectionResult, 
                                        output_file: Optional[str], 
                                        include_metadata: bool) -> Optional[str]:
        """Generate SARIF report from file results."""
        sarif_data = self.output_manager._convert_to_sarif(results)
        
        if include_metadata:
            sarif_data['metadata'] = {
                'generated_at': datetime.now().isoformat(),
                'levox_version': '0.9.0',
                'report_type': 'sarif'
            }
        
        # Always save to file for clean terminal output
        if not output_file:
            # Generate a default filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            scan_name = "scan_report"
            if hasattr(results, 'scan_path') and results.scan_path:
                scan_name = Path(results.scan_path).name
            elif isinstance(results, dict) and 'scan_path' in results:
                scan_name = Path(results['scan_path']).name
            
            output_file = f"levox_report_{scan_name}_{timestamp}.sarif"
        
        # Write to output file
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(sarif_data, f, indent=2, ensure_ascii=False)
        
        return str(output_path)
    
    def _prepare_report_data(self, results: DetectionResult, scan_time: float, 
                            license_tier: str) -> Dict[str, Any]:
        """Prepare comprehensive report data."""
        total_matches = sum(len(file_result.matches) for file_result in results.file_results)
        total_files = len(results.file_results)
        
        # Group issues by severity
        issues_by_severity = {'CRITICAL': [], 'HIGH': [], 'MEDIUM': [], 'LOW': []}
        for file_result in results.file_results:
            for match in file_result.matches:
                severity = self._calculate_severity(match)
                if severity in issues_by_severity:
                    issues_by_severity[severity].append({
                        'file': str(file_result.file_path),
                        'line': match.line_number,
                        'pattern': match.pattern_name,
                        'description': self._generate_description(match),
                        'confidence': match.confidence,
                        'matched_text': match.matched_text[:100] + "..." if len(match.matched_text) > 100 else match.matched_text
                    })
        
        return {
            'report_metadata': {
                'generated_at': datetime.now().isoformat(),
                'levox_version': '0.9.0',
                'license_tier': license_tier,
                'scan_time_seconds': scan_time
            },
            'scan_summary': {
                'total_files_scanned': total_files,
                'total_issues_found': total_matches,
                'scan_path': str(results.scan_path) if hasattr(results, 'scan_path') else None,
                'severity_distribution': {
                    severity: len(issues) for severity, issues in issues_by_severity.items()
                }
            },
            'issues_by_severity': issues_by_severity,
            'detailed_results': [
                {
                    'file_path': str(file_result.file_path),
                    'file_size_bytes': getattr(file_result, 'file_size', 0),
                    'language': getattr(file_result, 'language', 'unknown'),
                    'matches': [
                        {
                            'pattern_name': match.pattern_name,
                            'line_number': match.line_number,
                            'column_start': match.column_start,
                            'column_end': match.column_end,
                            'matched_text': match.matched_text,
                            'confidence': match.confidence,
                            'risk_level': str(match.risk_level),
                            'detection_level': match.metadata.get('detection_level', 'unknown'),
                            'metadata': match.metadata
                        }
                        for match in file_result.matches
                    ]
                }
                for file_result in results.file_results
            ]
        }
    
    def _prepare_sarif_data(self, results: DetectionResult, scan_time: float, 
                            license_tier: str) -> Dict[str, Any]:
        """Prepare SARIF format data with enhanced CI/CD metadata."""
        # Get CI/CD environment information
        ci_info = self._get_ci_environment_info()
        
        # Collect unique rules
        unique_rules = {}
        for file_result in results.file_results:
            for match in file_result.matches:
                if match.pattern_name not in unique_rules:
                    unique_rules[match.pattern_name] = {
                        "id": match.pattern_name,
                        "name": match.pattern_name,
                        "shortDescription": {"text": f"PII Detection: {match.pattern_name}"},
                        "fullDescription": {"text": self._get_pattern_description(match.pattern_name)},
                        "helpUri": f"https://github.com/levox/levox/docs/patterns#{match.pattern_name}",
                        "properties": {
                            "category": self._get_pattern_category(match.pattern_name),
                            "severity": self._calculate_severity(match),
                            "confidence": match.confidence
                        }
                    }
        
        return {
            "version": "2.1.0",
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "Levox",
                        "version": "0.9.0",
                        "informationUri": "https://levoxserver.vercel.app",
                        "fullName": "Levox Enterprise PII/GDPR Detection Tool",
                        "rules": list(unique_rules.values())
                    }
                },
                "invocations": [{
                    "executionSuccessful": True,
                    "startTimeUtc": datetime.now().isoformat(),
                    "endTimeUtc": datetime.now().isoformat(),
                    "toolExecutionNotifications": [],
                    "environmentVariables": ci_info.get("environment_variables", {}),
                    "workingDirectory": {
                        "uri": ci_info.get("working_directory", ".")
                    }
                }],
                "artifacts": [
                    {
                        "location": {"uri": str(file_result.file_path)},
                        "length": getattr(file_result, 'file_size', 0),
                        "mimeType": self._get_mime_type(file_result.file_path),
                        "sourceLanguage": self._get_source_language(file_result.file_path)
                    }
                    for file_result in results.file_results
                ],
                "results": [
                    {
                        "ruleId": match.pattern_name,
                        "level": self._get_sarif_level(match),
                        "message": {
                            "text": self._get_sarif_message(match),
                            "richText": self._get_rich_text_message(match)
                        },
                        "locations": [{
                            "physicalLocation": {
                                "artifactLocation": {"uri": str(file_result.file_path)},
                                "region": {
                                    "startLine": match.line_number,
                                    "startColumn": match.column_start,
                                    "endColumn": match.column_end,
                                    "snippet": {
                                        "text": match.matched_text[:200] + "..." if len(match.matched_text) > 200 else match.matched_text
                                    }
                                }
                            }
                        }],
                        "properties": {
                            "confidence": match.confidence,
                            "detection_level": match.metadata.get('detection_level', 'unknown'),
                            "license_tier": license_tier,
                            "severity": self._calculate_severity(match),
                            "category": self._get_pattern_category(match.pattern_name),
                            "remediation": self._get_remediation_guidance(match.pattern_name),
                            "ci_metadata": {
                                "scan_time": scan_time,
                                "environment": ci_info.get("environment", "unknown"),
                                "build_id": ci_info.get("build_id"),
                                "commit_hash": ci_info.get("commit_hash"),
                                "branch": ci_info.get("branch"),
                                "pull_request": ci_info.get("pull_request")
                            }
                        },
                        "fixes": self._get_sarif_fixes(match),
                        "relatedLocations": self._get_related_locations(match)
                    }
                    for file_result in results.file_results
                    for match in file_result.matches
                ],
                "properties": {
                    "scan_summary": {
                        "total_files_scanned": len(results.file_results),
                        "total_issues_found": sum(len(file_result.matches) for file_result in results.file_results),
                        "scan_time_seconds": scan_time,
                        "license_tier": license_tier,
                        "ci_environment": ci_info.get("environment", "unknown")
                    }
                }
            }]
        }
    
    def _generate_html_content(self, results: Union[DetectionResult, Dict[str, Any]], scan_time: float, 
                              license_tier: str, include_metadata: bool = False) -> str:
        """Generate HTML report content."""
        # Handle both DetectionResult objects and dictionaries
        if isinstance(results, dict):
            # Extract data from dictionary format
            file_results = results.get('file_results', [])
            total_matches = results.get('total_issues_found', 0)
            total_files = len(file_results)
            
            # If scan_time is 0, try to get it from the results
            if scan_time == 0.0 and 'scan_metadata' in results:
                scan_time = results['scan_metadata'].get('scan_time', 0.0)
        else:
            # Handle DetectionResult object
            file_results = results.file_results
            total_matches = sum(len(file_result.matches) for file_result in results.file_results)
            total_files = len(results.file_results)
        
        # Generate severity distribution
        severity_dist = {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
        for file_result in file_results:
            # Handle both object and dict formats
            if isinstance(file_result, dict):
                matches = file_result.get('matches', [])
                file_path = file_result.get('file_path', 'Unknown')
            else:
                matches = file_result.matches
                file_path = file_result.file_path
            
            for match in matches:
                # Handle both object and dict formats
                if isinstance(match, dict):
                    severity = self._calculate_severity_from_dict(match)
                else:
                    severity = self._calculate_severity(match)
                
                if severity in severity_dist:
                    severity_dist[severity] += 1
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Levox Security Scan Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
            margin-top: 10px;
        }}
        .content {{
            padding: 30px;
        }}
        .summary {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .summary-item {{
            text-align: center;
            padding: 15px;
            background: white;
            border-radius: 6px;
            border-left: 4px solid #667eea;
        }}
        .summary-number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        .summary-label {{
            color: #666;
            margin-top: 5px;
        }}
        .severity-badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: bold;
            color: white;
        }}
        .severity-critical {{ background-color: #dc3545; }}
        .severity-high {{ background-color: #fd7e14; }}
        .severity-medium {{ background-color: #ffc107; color: #212529; }}
        .severity-low {{ background-color: #28a745; }}
        .issues-section {{
            margin-top: 30px;
        }}
        .file-section {{
            margin-bottom: 30px;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            overflow: hidden;
        }}
        .file-header {{
            background: #f8f9fa;
            padding: 15px 20px;
            border-bottom: 1px solid #e9ecef;
            font-weight: bold;
            color: #495057;
        }}
        .issues-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .issues-table th {{
            background: #e9ecef;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            color: #495057;
        }}
        .issues-table td {{
            padding: 12px;
            border-bottom: 1px solid #e9ecef;
        }}
        .issues-table tr:hover {{
            background-color: #f8f9fa;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e9ecef;
        }}
        @media (max-width: 768px) {{
            .summary-grid {{
                grid-template-columns: 1fr;
            }}
            .issues-table {{
                font-size: 0.9em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔒 Levox Security Scan Report</h1>
            <div class="subtitle">PII Detection & GDPR Compliance Analysis</div>
        </div>
        
        <div class="content">
            <div class="summary">
                <h2>📊 Scan Summary</h2>
                <div class="summary-grid">
                    <div class="summary-item">
                        <div class="summary-number">{total_files}</div>
                        <div class="summary-label">Files Scanned</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{total_matches}</div>
                        <div class="summary-label">Issues Found</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{scan_time:.2f}s</div>
                        <div class="summary-label">Scan Time</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{license_tier.title()}</div>
                        <div class="summary-label">License Tier</div>
                    </div>
                </div>
                
                <h3>🚨 Severity Distribution</h3>
                <div class="summary-grid">
                    <div class="summary-item">
                        <div class="summary-number">{severity_dist['CRITICAL']}</div>
                        <div class="summary-label">Critical</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{severity_dist['HIGH']}</div>
                        <div class="summary-label">High</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{severity_dist['MEDIUM']}</div>
                        <div class="summary-label">Medium</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{severity_dist['LOW']}</div>
                        <div class="summary-label">Low</div>
                    </div>
                </div>
            </div>
            
            <div class="issues-section">
                <h2>🔍 Detailed Issues</h2>
        """
        
        # Add file sections
        for file_result in file_results:
            # Handle both object and dict formats
            if isinstance(file_result, dict):
                matches = file_result.get('matches', [])
                file_path = file_result.get('file_path', 'Unknown')
            else:
                matches = file_result.matches
                file_path = file_result.file_path
            
            if not matches:
                continue
                
            file_name = Path(file_path).name
            file_path_str = str(file_path)
            
            html += f"""
                <div class="file-section">
                    <div class="file-header">
                        📁 {file_name}
                        <div style="font-size: 0.8em; font-weight: normal; margin-top: 5px; color: #6c757d;">
                            {file_path_str}
                        </div>
                    </div>
                    <table class="issues-table">
                        <thead>
                            <tr>
                                <th>Line</th>
                                <th>Severity</th>
                                <th>Pattern</th>
                                <th>Description</th>
                                <th>Confidence</th>
                            </tr>
                        </thead>
                        <tbody>
            """
            
            for match in matches:
                # Handle both object and dict formats
                if isinstance(match, dict):
                    severity = self._calculate_severity_from_dict(match)
                    description = self._generate_description_from_dict(match)
                    confidence_pct = f"{match.get('confidence', 0):.1%}"
                    line_number = match.get('line_number', 0)
                    pattern_name = match.get('pattern_name', 'Unknown')
                else:
                    severity = self._calculate_severity(match)
                    description = self._generate_description(match)
                    confidence_pct = f"{match.confidence:.1%}"
                    line_number = match.line_number
                    pattern_name = match.pattern_name
                
                html += f"""
                            <tr>
                                <td>{line_number}</td>
                                <td><span class="severity-badge severity-{severity.lower()}">{severity}</span></td>
                                <td>{pattern_name}</td>
                                <td>{description}</td>
                                <td>{confidence_pct}</td>
                            </tr>
                """
            
            html += """
                        </tbody>
                    </table>
                </div>
            """
        
        # Add metadata if requested
        if include_metadata:
            html += f"""
                <div class="summary">
                    <h2>📋 Metadata</h2>
                    <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p><strong>Levox Version:</strong> 0.9.0</p>
                    <p><strong>Report Type:</strong> HTML</p>
                </div>
            """
        
        html += """
            </div>
        </div>
        
        <div class="footer">
            <p>Generated by Levox - Enterprise PII/GDPR Detection Tool</p>
            <p>🔒 Secure • 🚀 Fast • 🎯 Accurate</p>
        </div>
    </div>
</body>
</html>
        """
        
        return html
    
    def _calculate_severity(self, match) -> str:
        """Calculate severity for a detection match."""
        # Use the same logic as the output manager
        risk_value = getattr(match.risk_level, 'value', str(match.risk_level)).upper()
        confidence = match.confidence
        pattern_name = match.pattern_name.lower()
        
        # Base severity from risk level
        base_severity = {
            'CRITICAL': 4,
            'HIGH': 3,
            'MEDIUM': 2,
            'LOW': 1
        }.get(risk_value, 2)
        
        # Adjust based on confidence
        if confidence > 0.9:
            base_severity += 1
        elif confidence < 0.5:
            base_severity -= 1
        
        # Adjust based on pattern type
        if 'password' in pattern_name or 'secret' in pattern_name:
            base_severity += 1
        elif 'email' in pattern_name and confidence < 0.7:
            base_severity -= 1
        
        # Clamp to valid range
        base_severity = max(1, min(4, base_severity))
        
        severity_map = {4: 'CRITICAL', 3: 'HIGH', 2: 'MEDIUM', 1: 'LOW'}
        return severity_map[base_severity]
    
    def _generate_description(self, match) -> str:
        """Generate a description for a detection match."""
        pattern_name = match.pattern_name
        matched_text = match.matched_text
        
        descriptions = {
            'hardcoded_password': f"Hardcoded password found: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            'api_key': f"API key exposed in code: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            'email_address': f"Email address found: {matched_text}",
            'credit_card': f"Credit card number detected: {matched_text[:4]}****{matched_text[-4:]}",
            'ssn': f"Social Security Number detected: {matched_text[:3]}-**-{matched_text[-4:]}",
            'phone_number': f"Phone number found: {matched_text}",
            'ip_address': f"IP address found: {matched_text}",
            'database_url': f"Database connection string found: {matched_text.split('@')[0]}@***",
            'aws_access_key': f"AWS access key found: {matched_text[:20]}...",
            'private_key': f"Private key or certificate found in code"
        }
        
        return descriptions.get(pattern_name, f"Potential {pattern_name.replace('_', ' ')}: {matched_text}")

    def _generate_description_from_dict(self, match_dict: Dict[str, Any]) -> str:
        """Generate a description for a detection match from a dictionary."""
        pattern_name = match_dict.get('pattern_name', 'Unknown')
        matched_text = match_dict.get('matched_text', '')

        descriptions = {
            'hardcoded_password': f"Hardcoded password found: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            'api_key': f"API key exposed in code: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            'email_address': f"Email address found: {matched_text}",
            'credit_card': f"Credit card number detected: {matched_text[:4]}****{matched_text[-4:]}",
            'ssn': f"Social Security Number detected: {matched_text[:3]}-**-{matched_text[-4:]}",
            'phone_number': f"Phone number found: {matched_text}",
            'ip_address': f"IP address found: {matched_text}",
            'database_url': f"Database connection string found: {matched_text.split('@')[0]}@***",
            'aws_access_key': f"AWS access key found: {matched_text[:20]}...",
            'private_key': f"Private key or certificate found in code"
        }

        return descriptions.get(pattern_name, f"Potential {pattern_name.replace('_', ' ')}: {matched_text}")

    def _calculate_severity_from_dict(self, match_dict: Dict[str, Any]) -> str:
        """Calculate severity for a detection match from a dictionary."""
        risk_value = match_dict.get('risk_level', 'MEDIUM').upper()
        confidence = match_dict.get('confidence', 0.5)
        pattern_name = match_dict.get('pattern_name', 'Unknown').lower()

        # Base severity from risk level
        base_severity = {
            'CRITICAL': 4,
            'HIGH': 3,
            'MEDIUM': 2,
            'LOW': 1
        }.get(risk_value, 2)

        # Adjust based on confidence
        if confidence > 0.9:
            base_severity += 1
        elif confidence < 0.5:
            base_severity -= 1

        # Adjust based on pattern type
        if 'password' in pattern_name or 'secret' in pattern_name:
            base_severity += 1
        elif 'email' in pattern_name and confidence < 0.7:
            base_severity -= 1

        # Clamp to valid range
        base_severity = max(1, min(4, base_severity))

        severity_map = {4: 'CRITICAL', 3: 'HIGH', 2: 'MEDIUM', 1: 'LOW'}
        return severity_map[base_severity]

    def _restructure_scan_results(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """Restructure scan results to match expected format."""
        # Handle the actual scan results structure
        if 'results' in scan_results:
            # Convert 'results' to 'file_results' for compatibility
            restructured = {
                'file_results': scan_results['results'],
                'total_issues_found': scan_results.get('scan_summary', {}).get('total_matches', 0),
                'scan_path': scan_results.get('scan_summary', {}).get('scan_path', 'Unknown')
            }
            return restructured
        elif 'total_issues_found' in scan_results and 'file_results' not in scan_results:
            # Convert from summary format to detailed format
            restructured = {
                'file_results': [],
                'total_issues_found': scan_results.get('total_issues_found', 0),
                'scan_path': scan_results.get('scan_path', 'Unknown')
            }
            return restructured
        
        return scan_results
    
    def _get_ci_environment_info(self) -> Dict[str, Any]:
        """Get CI/CD environment information."""
        ci_info = {
            "environment": "unknown",
            "environment_variables": {},
            "working_directory": os.getcwd(),
            "build_id": None,
            "commit_hash": None,
            "branch": None,
            "pull_request": None
        }
        
        # Detect CI environment
        if os.getenv("GITHUB_ACTIONS"):
            ci_info.update({
                "environment": "github_actions",
                "build_id": os.getenv("GITHUB_RUN_ID"),
                "commit_hash": os.getenv("GITHUB_SHA"),
                "branch": os.getenv("GITHUB_REF_NAME"),
                "pull_request": os.getenv("GITHUB_PR_NUMBER"),
                "environment_variables": {
                    "GITHUB_REPOSITORY": os.getenv("GITHUB_REPOSITORY"),
                    "GITHUB_WORKFLOW": os.getenv("GITHUB_WORKFLOW"),
                    "GITHUB_ACTOR": os.getenv("GITHUB_ACTOR")
                }
            })
        elif os.getenv("GITLAB_CI"):
            ci_info.update({
                "environment": "gitlab_ci",
                "build_id": os.getenv("CI_PIPELINE_ID"),
                "commit_hash": os.getenv("CI_COMMIT_SHA"),
                "branch": os.getenv("CI_COMMIT_REF_NAME"),
                "pull_request": os.getenv("CI_MERGE_REQUEST_IID"),
                "environment_variables": {
                    "CI_PROJECT_NAME": os.getenv("CI_PROJECT_NAME"),
                    "CI_PIPELINE_URL": os.getenv("CI_PIPELINE_URL"),
                    "CI_COMMIT_AUTHOR": os.getenv("CI_COMMIT_AUTHOR")
                }
            })
        elif os.getenv("JENKINS_URL"):
            ci_info.update({
                "environment": "jenkins",
                "build_id": os.getenv("BUILD_NUMBER"),
                "commit_hash": os.getenv("GIT_COMMIT"),
                "branch": os.getenv("GIT_BRANCH"),
                "environment_variables": {
                    "JOB_NAME": os.getenv("JOB_NAME"),
                    "BUILD_URL": os.getenv("BUILD_URL"),
                    "GIT_COMMITTER_NAME": os.getenv("GIT_COMMITTER_NAME")
                }
            })
        elif os.getenv("AZURE_DEVOPS"):
            ci_info.update({
                "environment": "azure_devops",
                "build_id": os.getenv("BUILD_BUILDID"),
                "commit_hash": os.getenv("BUILD_SOURCEVERSION"),
                "branch": os.getenv("BUILD_SOURCEBRANCHNAME"),
                "pull_request": os.getenv("SYSTEM_PULLREQUEST_PULLREQUESTNUMBER"),
                "environment_variables": {
                    "BUILD_REPOSITORY_NAME": os.getenv("BUILD_REPOSITORY_NAME"),
                    "BUILD_DEFINITIONNAME": os.getenv("BUILD_DEFINITIONNAME"),
                    "BUILD_REQUESTEDFOR": os.getenv("BUILD_REQUESTEDFOR")
                }
            })
        elif os.getenv("CIRCLECI"):
            ci_info.update({
                "environment": "circleci",
                "build_id": os.getenv("CIRCLE_BUILD_NUM"),
                "commit_hash": os.getenv("CIRCLE_SHA1"),
                "branch": os.getenv("CIRCLE_BRANCH"),
                "pull_request": os.getenv("CIRCLE_PULL_REQUEST"),
                "environment_variables": {
                    "CIRCLE_PROJECT_REPONAME": os.getenv("CIRCLE_PROJECT_REPONAME"),
                    "CIRCLE_USERNAME": os.getenv("CIRCLE_USERNAME"),
                    "CIRCLE_WORKFLOW_ID": os.getenv("CIRCLE_WORKFLOW_ID")
                }
            })
        elif os.getenv("BITBUCKET_BUILD_NUMBER"):
            ci_info.update({
                "environment": "bitbucket_pipelines",
                "build_id": os.getenv("BITBUCKET_BUILD_NUMBER"),
                "commit_hash": os.getenv("BITBUCKET_COMMIT"),
                "branch": os.getenv("BITBUCKET_BRANCH"),
                "pull_request": os.getenv("BITBUCKET_PR_ID"),
                "environment_variables": {
                    "BITBUCKET_REPO_FULL_NAME": os.getenv("BITBUCKET_REPO_FULL_NAME"),
                    "BITBUCKET_STEP_UUID": os.getenv("BITBUCKET_STEP_UUID"),
                    "BITBUCKET_BUILD_NUMBER": os.getenv("BITBUCKET_BUILD_NUMBER")
                }
            })
        
        return ci_info
    
    def _get_pattern_description(self, pattern_name: str) -> str:
        """Get detailed description for a pattern."""
        descriptions = {
            "hardcoded_password": "Hardcoded passwords pose a significant security risk as they can be easily discovered in source code. Use environment variables or secure credential management systems instead.",
            "api_key": "API keys exposed in source code can be misused by unauthorized parties. Store API keys in secure environment variables or key management services.",
            "email_address": "Email addresses found in code may indicate PII exposure. Consider if this data should be externalized or anonymized.",
            "credit_card": "Credit card numbers in source code violate PCI DSS compliance requirements. Never store credit card data in code repositories.",
            "ssn": "Social Security Numbers are highly sensitive PII that should never be stored in source code. Use secure data storage solutions.",
            "phone_number": "Phone numbers may contain PII and should be handled according to privacy regulations like GDPR.",
            "ip_address": "IP addresses may be considered PII in certain jurisdictions and should be handled appropriately.",
            "database_url": "Database connection strings often contain sensitive credentials and should be externalized to environment variables.",
            "aws_access_key": "AWS access keys provide access to cloud resources and should never be stored in source code. Use IAM roles or secure key management.",
            "private_key": "Private keys and certificates should never be stored in source code repositories. Use secure key management systems."
        }
        return descriptions.get(pattern_name, f"Potential {pattern_name.replace('_', ' ')} detected in source code.")
    
    def _get_pattern_category(self, pattern_name: str) -> str:
        """Get category for a pattern."""
        categories = {
            "hardcoded_password": "Authentication",
            "api_key": "API Security",
            "email_address": "PII",
            "credit_card": "Financial Data",
            "ssn": "PII",
            "phone_number": "PII",
            "ip_address": "Network",
            "database_url": "Database",
            "aws_access_key": "Cloud Credentials",
            "private_key": "Cryptography"
        }
        return categories.get(pattern_name, "Security")
    
    def _get_sarif_level(self, match) -> str:
        """Get SARIF level for a match."""
        severity = self._calculate_severity(match)
        confidence = match.confidence
        
        if severity == "CRITICAL" and confidence > 0.9:
            return "error"
        elif severity in ["HIGH", "CRITICAL"] and confidence > 0.7:
            return "error"
        elif severity == "MEDIUM" and confidence > 0.8:
            return "warning"
        elif severity in ["MEDIUM", "LOW"] and confidence > 0.5:
            return "warning"
        else:
            return "note"
    
    def _get_sarif_message(self, match) -> str:
        """Get SARIF message for a match."""
        pattern_name = match.pattern_name
        matched_text = match.matched_text
        
        messages = {
            "hardcoded_password": f"Hardcoded password detected: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            "api_key": f"API key exposed in code: '{matched_text[:20]}{'...' if len(matched_text) > 20 else ''}'",
            "email_address": f"Email address found: {matched_text}",
            "credit_card": f"Credit card number detected: {matched_text[:4]}****{matched_text[-4:]}",
            "ssn": f"Social Security Number detected: {matched_text[:3]}-**-{matched_text[-4:]}",
            "phone_number": f"Phone number found: {matched_text}",
            "ip_address": f"IP address found: {matched_text}",
            "database_url": f"Database connection string found: {matched_text.split('@')[0]}@***",
            "aws_access_key": f"AWS access key found: {matched_text[:20]}...",
            "private_key": "Private key or certificate found in code"
        }
        
        return messages.get(pattern_name, f"Potential {pattern_name.replace('_', ' ')}: {matched_text}")
    
    def _get_rich_text_message(self, match) -> str:
        """Get rich text message for SARIF."""
        base_message = self._get_sarif_message(match)
        remediation = self._get_remediation_guidance(match.pattern_name)
        
        return f"{base_message}\n\n**Remediation:** {remediation}"
    
    def _get_remediation_guidance(self, pattern_name: str) -> str:
        """Get remediation guidance for a pattern."""
        guidance = {
            "hardcoded_password": "Store passwords in environment variables or use a secure credential management system like HashiCorp Vault or AWS Secrets Manager.",
            "api_key": "Move API keys to environment variables or use a secure key management service. Never commit API keys to version control.",
            "email_address": "Consider if email addresses need to be in source code. If required, use configuration files or environment variables.",
            "credit_card": "Never store credit card data in source code. Use PCI-compliant payment processors and tokenization services.",
            "ssn": "Social Security Numbers should never be stored in source code. Use secure databases with proper encryption and access controls.",
            "phone_number": "Store phone numbers in secure databases with proper access controls. Consider data anonymization techniques.",
            "ip_address": "IP addresses may be considered PII. Store in secure databases and implement proper access controls.",
            "database_url": "Move database connection strings to environment variables or configuration files outside of version control.",
            "aws_access_key": "Use IAM roles instead of access keys when possible. Store access keys in AWS Secrets Manager or similar services.",
            "private_key": "Store private keys in secure key management systems. Never commit private keys to version control."
        }
        return guidance.get(pattern_name, "Review the detected pattern and implement appropriate security measures.")
    
    def _get_sarif_fixes(self, match) -> List[Dict[str, Any]]:
        """Get SARIF fixes for a match."""
        fixes = []
        
        if match.pattern_name in ["hardcoded_password", "api_key", "database_url", "aws_access_key"]:
            fixes.append({
                "description": {
                    "text": "Replace hardcoded value with environment variable"
                },
                "artifactChanges": [{
                    "artifactLocation": {"uri": str(match.file_path)},
                    "replacements": [{
                        "deletedRegion": {
                            "startLine": match.line_number,
                            "startColumn": match.column_start,
                            "endColumn": match.column_end
                        },
                        "insertedContent": {
                            "text": f"os.getenv('{match.pattern_name.upper()}_KEY')"
                        }
                    }]
                }]
            })
        
        return fixes
    
    def _get_related_locations(self, match) -> List[Dict[str, Any]]:
        """Get related locations for a match."""
        related = []
        
        # Add related locations based on pattern type
        if match.pattern_name == "hardcoded_password":
            related.append({
                "id": 1,
                "physicalLocation": {
                    "artifactLocation": {"uri": "https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_credentials"},
                    "region": {"startLine": 1}
                },
                "message": {"text": "OWASP guidance on hardcoded credentials"}
            })
        
        return related
    
    def _get_mime_type(self, file_path: Path) -> str:
        """Get MIME type for a file."""
        mime_types = {
            ".py": "text/x-python",
            ".js": "text/javascript",
            ".ts": "text/typescript",
            ".java": "text/x-java-source",
            ".go": "text/x-go",
            ".rs": "text/x-rust",
            ".cpp": "text/x-c++",
            ".c": "text/x-c",
            ".h": "text/x-c",
            ".php": "text/x-php",
            ".rb": "text/x-ruby",
            ".swift": "text/x-swift",
            ".kt": "text/x-kotlin",
            ".scala": "text/x-scala",
            ".clj": "text/x-clojure",
            ".hs": "text/x-haskell",
            ".ml": "text/x-ocaml",
            ".fs": "text/x-fsharp",
            ".vb": "text/x-vb",
            ".cs": "text/x-csharp",
            ".dart": "text/x-dart",
            ".r": "text/x-r",
            ".m": "text/x-objective-c",
            ".pl": "text/x-perl",
            ".sh": "text/x-shellscript",
            ".bash": "text/x-shellscript",
            ".zsh": "text/x-shellscript",
            ".fish": "text/x-fish",
            ".ps1": "text/x-powershell",
            ".bat": "text/x-msdos-batch",
            ".cmd": "text/x-msdos-batch"
        }
        
        return mime_types.get(file_path.suffix.lower(), "text/plain")
    
    def _get_source_language(self, file_path: Path) -> str:
        """Get source language for a file."""
        languages = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".java": "java",
            ".go": "go",
            ".rs": "rust",
            ".cpp": "cpp",
            ".c": "c",
            ".h": "c",
            ".php": "php",
            ".rb": "ruby",
            ".swift": "swift",
            ".kt": "kotlin",
            ".scala": "scala",
            ".clj": "clojure",
            ".hs": "haskell",
            ".ml": "ocaml",
            ".fs": "fsharp",
            ".vb": "vb",
            ".cs": "csharp",
            ".dart": "dart",
            ".r": "r",
            ".m": "objective-c",
            ".pl": "perl",
            ".sh": "shell",
            ".bash": "shell",
            ".zsh": "shell",
            ".fish": "fish",
            ".ps1": "powershell",
            ".bat": "batch",
            ".cmd": "batch"
        }
        
        return languages.get(file_path.suffix.lower(), "unknown")
