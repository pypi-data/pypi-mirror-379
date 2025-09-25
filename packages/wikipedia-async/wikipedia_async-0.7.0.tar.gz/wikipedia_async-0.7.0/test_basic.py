#!/usr/bin/env python3
"""
Simple test to verify content and HTML functionality works.
"""

import asyncio
from wikipedia_async import WikipediaClient

async def test_basic_functionality():
    """Test basic content retrieval."""
    
    async with WikipediaClient() as client:
        print("Testing WikipediaClient content functionality...\n")
        
        # Test 1: Basic page (should always have extract/summary)
        print("1. Testing basic page retrieval...")
        page = await client.get_page("Python (programming language)")
        
        print(f"✅ Title: {page.title}")
        print(f"✅ Has extract/summary: {page.extract is not None}")
        if page.extract:
            print(f"✅ Extract length: {len(page.extract)} characters")
        
        # Test 2: Page with content
        print("\n2. Testing page with full content...")
        page_with_content = await client.get_page(
            "Python (programming language)", 
            include_content=True
        )
        
        print(f"✅ Has content: {page_with_content.content is not None}")
        if page_with_content.content:
            print(f"✅ Content length: {len(page_with_content.content)} characters")
        
        # Test 3: Direct content method
        print("\n3. Testing direct content method...")
        try:
            content = await client.get_page_content("Python (programming language)")
            print(f"✅ Direct content method works: {len(content)} characters")
        except Exception as e:
            print(f"❌ Direct content method failed: {e}")
        
        # Test 4: Direct HTML method  
        print("\n4. Testing direct HTML method...")
        try:
            html = await client.get_page_html("Python (programming language)")
            print(f"✅ Direct HTML method works: {len(html)} characters")
        except Exception as e:
            print(f"❌ Direct HTML method failed: {e}")
        
        print("\n✅ All basic tests completed!")

if __name__ == "__main__":
    asyncio.run(test_basic_functionality())