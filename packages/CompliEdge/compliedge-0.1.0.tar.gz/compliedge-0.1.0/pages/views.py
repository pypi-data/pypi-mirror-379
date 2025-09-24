from django.shortcuts import render

def about(request):
    """About page view"""
    return render(request, 'pages/about.html')

def blog(request):
    """Blog list page view"""
    # Sample blog posts data
    blog_posts = [
        {
            'id': 1,
            'title': 'Understanding GRC in the Modern Enterprise',
            'date': 'September 15, 2025',
            'summary': 'Learn how Governance, Risk, and Compliance frameworks are evolving to meet modern business challenges.',
            'author': 'CompliEdge Team'
        },
        {
            'id': 2,
            'title': 'Top 5 Cybersecurity Risks for 2025',
            'date': 'September 10, 2025',
            'summary': 'Discover the most critical cybersecurity threats organizations should prepare for this year.',
            'author': 'Security Team'
        },
        {
            'id': 3,
            'title': 'Compliance Automation Best Practices',
            'date': 'September 5, 2025',
            'summary': 'How to streamline your compliance processes with automation while maintaining regulatory adherence.',
            'author': 'Compliance Team'
        },
        {
            'id': 4,
            'title': 'Risk Assessment in the Age of AI',
            'date': 'August 28, 2025',
            'summary': 'Exploring how artificial intelligence is changing the landscape of risk management.',
            'author': 'Risk Team'
        }
    ]
    return render(request, 'pages/blog.html', {'blog_posts': blog_posts})

def blog_detail(request, post_id):
    """Blog detail page view"""
    # Sample blog post data
    blog_post = {
        'id': post_id,
        'title': 'Understanding GRC in the Modern Enterprise',
        'date': 'September 15, 2025',
        'author': 'CompliEdge Team',
        'content': '''
        <p>Governance, Risk, and Compliance (GRC) has become a critical component of modern enterprise operations. As organizations face increasingly complex regulatory environments and evolving threats, the need for integrated GRC solutions has never been greater.</p>
        
        <h2 class="text-xl font-semibold mt-6 mb-3">The Evolution of GRC</h2>
        <p>Traditional GRC approaches often involved siloed processes and disconnected tools. Today's organizations require integrated platforms that can provide real-time insights across all three domains. This shift has been driven by several factors:</p>
        <ul class="list-disc list-inside ml-4 mt-2 space-y-1">
            <li>Increasing regulatory complexity</li>
            <li>Rising cybersecurity threats</li>
            <li>Digital transformation initiatives</li>
            <li>Remote and hybrid work models</li>
        </ul>
        
        <h2 class="text-xl font-semibold mt-6 mb-3">Benefits of Integrated GRC</h2>
        <p>Organizations that implement integrated GRC solutions typically see significant improvements in:</p>
        <ul class="list-disc list-inside ml-4 mt-2 space-y-1">
            <li>Operational efficiency</li>
            <li>Risk visibility</li>
            <li>Compliance assurance</li>
            <li>Decision-making speed</li>
        </ul>
        
        <h2 class="text-xl font-semibold mt-6 mb-3">Future of GRC</h2>
        <p>As we look ahead, GRC will continue to evolve with emerging technologies like artificial intelligence, machine learning, and blockchain. These innovations will enable more proactive and predictive approaches to governance, risk management, and compliance.</p>
        '''
    }
    return render(request, 'pages/blog_detail.html', {'blog_post': blog_post})

def jobs(request):
    """Jobs page view"""
    return render(request, 'pages/jobs.html')

def press(request):
    """Press page view"""
    return render(request, 'pages/press.html')

def privacy(request):
    """Privacy Policy page view"""
    return render(request, 'pages/privacy.html')

def terms(request):
    """Terms & Conditions page view"""
    return render(request, 'pages/terms.html')